"""
API endpoints for n8n integration with appointment system
"""

from flask import Blueprint, jsonify, request, current_app
from flask_login import login_required, current_user
from app import db, mail
from app.models import (Appointment, AppointmentStatus, AppointmentType, 
                       AppointmentHistory, AppointmentHistoryAction, User)
from app.utils.appointment_automation import AppointmentAutomation
from datetime import datetime, timedelta
from sqlalchemy import and_, or_
import json
import pandas as pd
from io import BytesIO
import base64
import hmac
import hashlib
from functools import wraps

api = Blueprint('api', __name__, url_prefix='/api')

def verify_api_key(f):
    """Decorator to verify API key for n8n integration"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        expected_key = current_app.config.get('N8N_API_KEY', 'default-api-key')
        
        if not api_key or api_key != expected_key:
            return jsonify({'error': 'Invalid API key'}), 401
        
        return f(*args, **kwargs)
    return decorated_function

def verify_webhook_signature(f):
    """Decorator to verify webhook signature"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        signature = request.headers.get('X-Webhook-Signature')
        secret = current_app.config.get('WEBHOOK_SECRET', 'default-secret')
        
        if signature:
            expected_signature = hmac.new(
                secret.encode('utf-8'),
                request.data,
                hashlib.sha256
            ).hexdigest()
            
            if not hmac.compare_digest(f'sha256={expected_signature}', signature):
                return jsonify({'error': 'Invalid signature'}), 401
        
        return f(*args, **kwargs)
    return decorated_function

@api.route('/appointments/old', methods=['GET'])
@verify_api_key
def get_old_appointments():
    """Get old appointments for daily export"""
    try:
        # Get yesterday's date
        yesterday = datetime.now() - timedelta(days=1)
        start_of_yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_yesterday = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
        
        # Get old appointments
        old_appointments = Appointment.query.filter(
            or_(
                # Appointments from yesterday
                and_(
                    Appointment.scheduled_date >= start_of_yesterday,
                    Appointment.scheduled_date <= end_of_yesterday
                ),
                # Or completed/cancelled appointments from last week
                and_(
                    Appointment.status.in_([AppointmentStatus.COMPLETED, AppointmentStatus.CANCELLED]),
                    Appointment.updated_at >= datetime.now() - timedelta(days=7)
                )
            )
        ).order_by(Appointment.scheduled_date.desc()).all()
        
        appointments_data = []
        for appointment in old_appointments:
            data = appointment.to_dict()
            data['creator_username'] = appointment.creator.username if appointment.creator else None
            appointments_data.append(data)
        
        return jsonify({
            'success': True,
            'appointments': appointments_data,
            'count': len(appointments_data),
            'export_date': datetime.now().isoformat()
        })
        
    except Exception as e:
        current_app.logger.error(f"Error getting old appointments: {str(e)}")
        return jsonify({'error': str(e)}), 500

@api.route('/appointments/upcoming', methods=['GET'])
@verify_api_key
def get_upcoming_appointments():
    """Get upcoming appointments for reminder processing"""
    try:
        # Get appointments for next 3 days
        now = datetime.now()
        three_days_from_now = now + timedelta(days=3)
        
        upcoming_appointments = Appointment.query.filter(
            and_(
                Appointment.scheduled_date >= now,
                Appointment.scheduled_date <= three_days_from_now,
                Appointment.status.in_([AppointmentStatus.SCHEDULED, AppointmentStatus.CONFIRMED])
            )
        ).order_by(Appointment.scheduled_date.asc()).all()
        
        appointments_data = []
        for appointment in upcoming_appointments:
            data = appointment.to_dict()
            data['creator_username'] = appointment.creator.username if appointment.creator else None
            data['reminder_sent'] = appointment.reminder_sent
            appointments_data.append(data)
        
        return jsonify({
            'success': True,
            'appointments': appointments_data,
            'count': len(appointments_data)
        })
        
    except Exception as e:
        current_app.logger.error(f"Error getting upcoming appointments: {str(e)}")
        return jsonify({'error': str(e)}), 500

@api.route('/appointments/export/excel', methods=['POST'])
@verify_api_key
def generate_excel_export():
    """Generate Excel export from appointments data"""
    try:
        appointments_data = request.json.get('appointments', [])
        
        if not appointments_data:
            return jsonify({'error': 'No appointments data provided'}), 400
        
        # Create DataFrame
        df = pd.DataFrame(appointments_data)
        
        # Create Excel file in memory
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Appointments', index=False)
            
            # Add summary sheet
            summary_data = {
                'Metric': ['Total Appointments', 'Completed', 'Cancelled', 'Scheduled', 'Confirmed'],
                'Count': [
                    len(appointments_data),
                    len([a for a in appointments_data if a.get('status') == 'completed']),
                    len([a for a in appointments_data if a.get('status') == 'cancelled']),
                    len([a for a in appointments_data if a.get('status') == 'scheduled']),
                    len([a for a in appointments_data if a.get('status') == 'confirmed'])
                ]
            }
            summary_df = pd.DataFrame(summary_data)
            summary_df.to_excel(writer, sheet_name='Summary', index=False)
        
        output.seek(0)
        excel_data = output.getvalue()
        
        # Convert to base64 for JSON response
        excel_base64 = base64.b64encode(excel_data).decode('utf-8')
        
        return jsonify({
            'success': True,
            'excel_data': excel_base64,
            'filename': f"appointments_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
            'size_bytes': len(excel_data)
        })
        
    except Exception as e:
        current_app.logger.error(f"Error generating Excel export: {str(e)}")
        return jsonify({'error': str(e)}), 500

@api.route('/appointments/export/daily', methods=['POST'])
@verify_api_key
def trigger_daily_export():
    """Trigger daily export process"""
    try:
        automation = AppointmentAutomation()
        automation.daily_export_task()
        
        return jsonify({
            'success': True,
            'message': 'Daily export triggered successfully',
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        current_app.logger.error(f"Error triggering daily export: {str(e)}")
        return jsonify({'error': str(e)}), 500

@api.route('/appointments/<public_id>/reminder', methods=['POST'])
@verify_api_key
def send_appointment_reminder(public_id):
    """Send reminder email for specific appointment"""
    try:
        appointment = Appointment.query.filter_by(public_id=public_id).first()
        if not appointment:
            return jsonify({'error': 'Appointment not found'}), 404
        
        # Import the function from routes_appointments
        from app.routes_appointments import send_appointment_email
        
        success = send_appointment_email(appointment, 'reminder')
        
        if success:
            appointment.reminder_sent = True
            
            # Create history record
            history = AppointmentHistory(
                action=AppointmentHistoryAction.REMINDER_SENT,
                details=f"Reminder email sent via API to {appointment.client_email}",
                appointment_id=appointment.id,
                user_id=appointment.user_id
            )
            db.session.add(history)
            db.session.commit()
            
            return jsonify({
                'success': True,
                'message': 'Reminder email sent successfully',
                'appointment_id': public_id
            })
        else:
            return jsonify({'error': 'Failed to send reminder email'}), 500
        
    except Exception as e:
        current_app.logger.error(f"Error sending reminder for appointment {public_id}: {str(e)}")
        return jsonify({'error': str(e)}), 500

@api.route('/appointments/webhook', methods=['POST'])
@verify_webhook_signature
def appointment_webhook():
    """Webhook endpoint for appointment events"""
    try:
        data = request.json
        action = data.get('action')
        appointment_data = data.get('appointment')
        
        if not action or not appointment_data:
            return jsonify({'error': 'Missing action or appointment data'}), 400
        
        appointment_id = appointment_data.get('id')
        appointment = Appointment.query.filter_by(public_id=appointment_id).first()
        
        if not appointment:
            return jsonify({'error': 'Appointment not found'}), 404
        
        # Process different actions
        if action == 'appointment_created':
            # Send confirmation email
            from app.routes_appointments import send_appointment_email
            send_appointment_email(appointment, 'confirmation')
            
        elif action == 'appointment_updated':
            # Send update notification
            from app.routes_appointments import send_appointment_email
            send_appointment_email(appointment, 'update')
            
        elif action == 'appointment_cancelled':
            # Send cancellation notification
            from app.routes_appointments import send_appointment_email
            extra_data = {'reason': data.get('reason', 'No reason provided')}
            send_appointment_email(appointment, 'cancellation', extra_data)
            
        elif action == 'appointment_rescheduled':
            # Send reschedule notification
            from app.routes_appointments import send_appointment_email
            extra_data = {'reason': data.get('reason', 'Schedule change requested')}
            send_appointment_email(appointment, 'reschedule', extra_data)
        
        # Create history record for webhook processing
        history = AppointmentHistory(
            action=AppointmentHistoryAction.EMAIL_SENT,
            details=f"Webhook processed: {action}",
            appointment_id=appointment.id,
            user_id=appointment.user_id
        )
        db.session.add(history)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': f'Webhook processed successfully for action: {action}',
            'appointment_id': appointment_id
        })
        
    except Exception as e:
        current_app.logger.error(f"Error processing webhook: {str(e)}")
        return jsonify({'error': str(e)}), 500

@api.route('/appointments/stats', methods=['GET'])
@verify_api_key
def get_appointment_stats():
    """Get appointment statistics for dashboards"""
    try:
        # Overall stats
        total_appointments = Appointment.query.count()
        today = datetime.now().date()
        
        stats = {
            'total_appointments': total_appointments,
            'today_appointments': Appointment.query.filter(
                db.func.date(Appointment.scheduled_date) == today
            ).count(),
            'upcoming_appointments': Appointment.query.filter(
                and_(
                    Appointment.scheduled_date > datetime.now(),
                    Appointment.status.in_([AppointmentStatus.SCHEDULED, AppointmentStatus.CONFIRMED])
                )
            ).count(),
            'completed_appointments': Appointment.query.filter_by(
                status=AppointmentStatus.COMPLETED
            ).count(),
            'cancelled_appointments': Appointment.query.filter_by(
                status=AppointmentStatus.CANCELLED
            ).count(),
            'by_type': {},
            'by_status': {},
            'recent_activity': []
        }
        
        # Stats by type
        for appointment_type in AppointmentType:
            count = Appointment.query.filter_by(appointment_type=appointment_type).count()
            stats['by_type'][appointment_type.value] = count
        
        # Stats by status
        for status in AppointmentStatus:
            count = Appointment.query.filter_by(status=status).count()
            stats['by_status'][status.value] = count
        
        # Recent activity (last 10 appointments)
        recent_appointments = Appointment.query.order_by(
            Appointment.created_at.desc()
        ).limit(10).all()
        
        for appointment in recent_appointments:
            stats['recent_activity'].append({
                'id': appointment.public_id,
                'title': appointment.title,
                'client_name': appointment.client_name,
                'status': appointment.status.value,
                'scheduled_date': appointment.scheduled_date.isoformat(),
                'created_at': appointment.created_at.isoformat()
            })
        
        return jsonify({
            'success': True,
            'stats': stats,
            'generated_at': datetime.now().isoformat()
        })
        
    except Exception as e:
        current_app.logger.error(f"Error getting appointment stats: {str(e)}")
        return jsonify({'error': str(e)}), 500

@api.route('/appointments/calendar', methods=['GET'])
@verify_api_key
def get_calendar_events():
    """Get appointments formatted for calendar integration"""
    try:
        start_date = request.args.get('start')
        end_date = request.args.get('end')
        
        query = Appointment.query
        
        if start_date:
            start_dt = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
            query = query.filter(Appointment.scheduled_date >= start_dt)
        
        if end_date:
            end_dt = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
            query = query.filter(Appointment.scheduled_date <= end_dt)
        
        appointments = query.filter(
            Appointment.status != AppointmentStatus.CANCELLED
        ).all()
        
        events = []
        for appointment in appointments:
            end_time = appointment.scheduled_date + timedelta(minutes=appointment.duration_minutes)
            
            # Color code by status
            color_map = {
                'scheduled': '#007bff',  # Blue
                'confirmed': '#28a745',  # Green
                'completed': '#6c757d',  # Gray
                'no_show': '#dc3545',    # Red
                'rescheduled': '#ffc107' # Yellow
            }
            
            events.append({
                'id': appointment.public_id,
                'title': f"{appointment.title} - {appointment.client_name}",
                'start': appointment.scheduled_date.isoformat(),
                'end': end_time.isoformat(),
                'description': f"Client: {appointment.client_name}\nType: {appointment.appointment_type.value}\nStatus: {appointment.status.value}",
                'color': color_map.get(appointment.status.value, '#007bff'),
                'url': f"/appointments/{appointment.public_id}",
                'extendedProps': {
                    'appointment_type': appointment.appointment_type.value,
                    'status': appointment.status.value,
                    'client_email': appointment.client_email,
                    'client_phone': appointment.client_phone,
                    'meeting_location': appointment.meeting_location,
                    'meeting_link': appointment.meeting_link
                }
            })
        
        return jsonify({
            'success': True,
            'events': events,
            'count': len(events)
        })
        
    except Exception as e:
        current_app.logger.error(f"Error getting calendar events: {str(e)}")
        return jsonify({'error': str(e)}), 500