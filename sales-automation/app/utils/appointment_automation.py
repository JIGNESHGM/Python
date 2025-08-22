"""
Daily Automation Tasks for Appointment System
This module handles scheduled tasks like daily Excel exports and email notifications.
"""

import os
import pandas as pd
from datetime import datetime, timedelta
from io import BytesIO
from flask import current_app
from flask_mail import Message
from app import db, mail
from app.models import Appointment, AppointmentStatus, AppointmentHistory, AppointmentHistoryAction, User
import schedule
import time
import threading
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AppointmentAutomation:
    """Handles automated appointment tasks"""
    
    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)
    
    def init_app(self, app):
        """Initialize automation with Flask app"""
        self.app = app
        # Schedule daily export at 8:00 AM
        schedule.every().day.at("08:00").do(self.daily_export_task)
        
        # Schedule reminder emails 24 hours before appointments
        schedule.every(30).minutes.do(self.send_appointment_reminders)
        
        # Schedule follow-up emails for completed appointments
        schedule.every().day.at("09:00").do(self.send_followup_emails)
        
        # Start scheduler in background thread
        scheduler_thread = threading.Thread(target=self.run_scheduler)
        scheduler_thread.daemon = True
        scheduler_thread.start()
        
        logger.info("Appointment automation initialized")
    
    def run_scheduler(self):
        """Run the scheduler in background"""
        while True:
            try:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
            except Exception as e:
                logger.error(f"Scheduler error: {str(e)}")
                time.sleep(300)  # Wait 5 minutes before retrying
    
    def daily_export_task(self):
        """Daily task to export old appointments and send to admin"""
        try:
            with self.app.app_context():
                logger.info("Starting daily appointment export task")
                
                # Get yesterday's date
                yesterday = datetime.now() - timedelta(days=1)
                start_of_yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
                end_of_yesterday = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
                
                # Get old appointments (completed, cancelled, or past scheduled)
                old_appointments = Appointment.query.filter(
                    db.or_(
                        # Appointments from yesterday
                        db.and_(
                            Appointment.scheduled_date >= start_of_yesterday,
                            Appointment.scheduled_date <= end_of_yesterday
                        ),
                        # Or completed/cancelled appointments from last week
                        db.and_(
                            Appointment.status.in_([AppointmentStatus.COMPLETED, AppointmentStatus.CANCELLED]),
                            Appointment.updated_at >= datetime.now() - timedelta(days=7)
                        )
                    )
                ).order_by(Appointment.scheduled_date.desc()).all()
                
                if not old_appointments:
                    logger.info("No old appointments found for export")
                    return
                
                # Create Excel file
                excel_data = self.create_excel_export(old_appointments)
                filename = f"appointments_export_{datetime.now().strftime('%Y%m%d')}.xlsx"
                
                # Send email to admin users
                admin_users = User.query.filter_by(role='ADMIN').all()
                if not admin_users:
                    # If no admin users, send to all users
                    admin_users = User.query.filter_by(is_active=True).all()
                
                for admin in admin_users:
                    self.send_export_email(admin.email, excel_data, filename, len(old_appointments))
                
                # Upload to Google Sheets if configured
                self.upload_to_google_sheets(old_appointments)
                
                logger.info(f"Daily export completed. Exported {len(old_appointments)} appointments")
                
        except Exception as e:
            logger.error(f"Daily export task failed: {str(e)}")
    
    def create_excel_export(self, appointments):
        """Create Excel file from appointments data"""
        data = []
        for appointment in appointments:
            # Get appointment history
            history_records = AppointmentHistory.query.filter_by(appointment_id=appointment.id)\
                                                    .order_by(AppointmentHistory.created_at.desc()).all()
            
            history_summary = "; ".join([
                f"{h.action.value}: {h.created_at.strftime('%Y-%m-%d %H:%M')}"
                for h in history_records[:5]  # Last 5 actions
            ])
            
            data.append({
                'Appointment ID': appointment.public_id,
                'Title': appointment.title,
                'Type': appointment.appointment_type.value.replace('_', ' ').title(),
                'Status': appointment.status.value.replace('_', ' ').title(),
                'Client Name': appointment.client_name,
                'Client Email': appointment.client_email,
                'Client Phone': appointment.client_phone or '',
                'Client Company': appointment.client_company or '',
                'Scheduled Date': appointment.scheduled_date.strftime('%Y-%m-%d %H:%M'),
                'Duration (minutes)': appointment.duration_minutes,
                'Timezone': appointment.timezone,
                'Meeting Location': appointment.meeting_location or '',
                'Meeting Link': appointment.meeting_link or '',
                'Notes': appointment.notes or '',
                'Created At': appointment.created_at.strftime('%Y-%m-%d %H:%M'),
                'Updated At': appointment.updated_at.strftime('%Y-%m-%d %H:%M'),
                'Created By': appointment.creator.username if appointment.creator else '',
                'Recent History': history_summary
            })
        
        df = pd.DataFrame(data)
        
        # Create Excel file in memory
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Appointments', index=False)
            
            # Add summary sheet
            summary_data = {
                'Metric': ['Total Appointments', 'Completed', 'Cancelled', 'No Show', 'Rescheduled'],
                'Count': [
                    len(appointments),
                    len([a for a in appointments if a.status == AppointmentStatus.COMPLETED]),
                    len([a for a in appointments if a.status == AppointmentStatus.CANCELLED]),
                    len([a for a in appointments if a.status == AppointmentStatus.NO_SHOW]),
                    len([a for a in appointments if a.status == AppointmentStatus.RESCHEDULED])
                ]
            }
            summary_df = pd.DataFrame(summary_data)
            summary_df.to_excel(writer, sheet_name='Summary', index=False)
        
        output.seek(0)
        return output.getvalue()
    
    def send_export_email(self, recipient_email, excel_data, filename, appointment_count):
        """Send daily export email to admin"""
        try:
            subject = f"Daily Appointment Export - {datetime.now().strftime('%Y-%m-%d')} ({appointment_count} appointments)"
            
            body = f"""
            Dear Admin,
            
            Please find attached the daily appointment export for {datetime.now().strftime('%Y-%m-%d')}.
            
            Export Summary:
            - Total appointments: {appointment_count}
            - Export generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            
            The attached Excel file contains detailed information about all appointments from yesterday
            and recently completed/cancelled appointments.
            
            Best regards,
            Appointment System
            """
            
            msg = Message(
                subject=subject,
                recipients=[recipient_email],
                body=body
            )
            
            # Attach Excel file
            msg.attach(
                filename,
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                excel_data
            )
            
            mail.send(msg)
            logger.info(f"Export email sent to {recipient_email}")
            
        except Exception as e:
            logger.error(f"Failed to send export email to {recipient_email}: {str(e)}")
    
    def upload_to_google_sheets(self, appointments):
        """Upload appointment data to Google Sheets"""
        try:
            # This would require Google Sheets API setup
            # For now, we'll just log that this feature is available
            logger.info("Google Sheets integration available - implement with google-auth and gspread libraries")
            
            # Example implementation:
            # import gspread
            # from google.oauth2.service_account import Credentials
            # 
            # scopes = ["https://www.googleapis.com/auth/spreadsheets"]
            # creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
            # client = gspread.authorize(creds)
            # 
            # sheet = client.open("Appointment Exports").sheet1
            # data = [[a.title, a.client_name, a.scheduled_date.isoformat(), a.status.value] for a in appointments]
            # sheet.append_rows(data)
            
        except Exception as e:
            logger.error(f"Google Sheets upload failed: {str(e)}")
    
    def send_appointment_reminders(self):
        """Send reminder emails for appointments 24 hours in advance"""
        try:
            with self.app.app_context():
                # Get appointments scheduled for tomorrow
                tomorrow = datetime.now() + timedelta(days=1)
                start_of_tomorrow = tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)
                end_of_tomorrow = tomorrow.replace(hour=23, minute=59, second=59, microsecond=999999)
                
                upcoming_appointments = Appointment.query.filter(
                    db.and_(
                        Appointment.scheduled_date >= start_of_tomorrow,
                        Appointment.scheduled_date <= end_of_tomorrow,
                        Appointment.status.in_([AppointmentStatus.SCHEDULED, AppointmentStatus.CONFIRMED]),
                        Appointment.reminder_sent == False
                    )
                ).all()
                
                for appointment in upcoming_appointments:
                    if self.send_reminder_email(appointment):
                        appointment.reminder_sent = True
                        
                        # Create history record
                        history = AppointmentHistory(
                            action=AppointmentHistoryAction.REMINDER_SENT,
                            details=f"24-hour reminder email sent to {appointment.client_email}",
                            appointment_id=appointment.id,
                            user_id=appointment.user_id
                        )
                        db.session.add(history)
                
                db.session.commit()
                
                if upcoming_appointments:
                    logger.info(f"Sent {len(upcoming_appointments)} appointment reminders")
                
        except Exception as e:
            logger.error(f"Reminder email task failed: {str(e)}")
    
    def send_reminder_email(self, appointment):
        """Send reminder email for a specific appointment"""
        try:
            subject = f"Appointment Reminder - {appointment.title}"
            
            body = f"""
            Dear {appointment.client_name},
            
            This is a friendly reminder about your upcoming appointment:
            
            Title: {appointment.title}
            Date & Time: {appointment.scheduled_date.strftime('%Y-%m-%d at %H:%M')} ({appointment.timezone})
            Duration: {appointment.duration_minutes} minutes
            Type: {appointment.appointment_type.value.replace('_', ' ').title()}
            
            """
            
            if appointment.meeting_location:
                body += f"Location: {appointment.meeting_location}\n"
            
            if appointment.meeting_link:
                body += f"Meeting Link: {appointment.meeting_link}\n"
            
            if appointment.notes:
                body += f"\nNotes: {appointment.notes}\n"
            
            body += f"""
            If you need to reschedule or cancel this appointment, please contact us as soon as possible.
            
            We look forward to meeting with you!
            
            Best regards,
            {appointment.creator.username if appointment.creator else 'Appointment System'}
            """
            
            msg = Message(
                subject=subject,
                recipients=[appointment.client_email],
                body=body
            )
            
            mail.send(msg)
            return True
            
        except Exception as e:
            logger.error(f"Failed to send reminder email for appointment {appointment.public_id}: {str(e)}")
            return False
    
    def send_followup_emails(self):
        """Send follow-up emails for completed appointments"""
        try:
            with self.app.app_context():
                # Get appointments completed yesterday
                yesterday = datetime.now() - timedelta(days=1)
                start_of_yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
                end_of_yesterday = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
                
                completed_appointments = Appointment.query.filter(
                    db.and_(
                        Appointment.status == AppointmentStatus.COMPLETED,
                        Appointment.updated_at >= start_of_yesterday,
                        Appointment.updated_at <= end_of_yesterday
                    )
                ).all()
                
                for appointment in completed_appointments:
                    # Check if follow-up email already sent
                    followup_sent = AppointmentHistory.query.filter_by(
                        appointment_id=appointment.id,
                        action=AppointmentHistoryAction.EMAIL_SENT
                    ).filter(AppointmentHistory.details.contains('follow-up')).first()
                    
                    if not followup_sent:
                        if self.send_followup_email(appointment):
                            # Create history record
                            history = AppointmentHistory(
                                action=AppointmentHistoryAction.EMAIL_SENT,
                                details=f"Follow-up email sent to {appointment.client_email}",
                                appointment_id=appointment.id,
                                user_id=appointment.user_id
                            )
                            db.session.add(history)
                
                db.session.commit()
                
                if completed_appointments:
                    logger.info(f"Sent {len(completed_appointments)} follow-up emails")
                
        except Exception as e:
            logger.error(f"Follow-up email task failed: {str(e)}")
    
    def send_followup_email(self, appointment):
        """Send follow-up email for completed appointment"""
        try:
            subject = f"Thank you for your appointment - {appointment.title}"
            
            body = f"""
            Dear {appointment.client_name},
            
            Thank you for your time during our {appointment.appointment_type.value.replace('_', ' ').lower()} on {appointment.scheduled_date.strftime('%Y-%m-%d')}.
            
            We hope you found our meeting valuable and informative. If you have any questions or would like to schedule a follow-up meeting, please don't hesitate to contact us.
            
            We appreciate your business and look forward to working with you.
            
            Best regards,
            {appointment.creator.username if appointment.creator else 'Our Team'}
            """
            
            msg = Message(
                subject=subject,
                recipients=[appointment.client_email],
                body=body
            )
            
            mail.send(msg)
            return True
            
        except Exception as e:
            logger.error(f"Failed to send follow-up email for appointment {appointment.public_id}: {str(e)}")
            return False

# Initialize automation
automation = AppointmentAutomation()

def init_automation(app):
    """Initialize automation with Flask app"""
    automation.init_app(app)
    return automation