from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, current_app, abort
from flask_login import login_required, current_user
from app import db, mail
from app.models import (Appointment, AppointmentStatus, AppointmentType, AppointmentHistory, 
                       AppointmentHistoryAction, User, Lead)
from app.forms_appointment import (AppointmentForm, AppointmentUpdateForm, AppointmentRescheduleForm,
                                 AppointmentCancelForm, AppointmentSearchForm, BulkAppointmentActionForm)
from datetime import datetime, timedelta
from sqlalchemy import func, or_, and_
import pandas as pd
import os
import json
from io import BytesIO
from flask import send_file
from flask_mail import Message

appointments = Blueprint('appointments', __name__, url_prefix='/appointments')

@appointments.route('/')
@login_required
def index():
    """Main appointments dashboard"""
    # Get filter parameters
    search_form = AppointmentSearchForm()
    
    # Base query
    query = Appointment.query.filter_by(user_id=current_user.id)
    
    # Apply filters if provided
    if request.args.get('search'):
        search_term = request.args.get('search')
        query = query.filter(or_(
            Appointment.title.contains(search_term),
            Appointment.client_name.contains(search_term),
            Appointment.client_email.contains(search_term),
            Appointment.client_company.contains(search_term)
        ))
    
    if request.args.get('status'):
        status = request.args.get('status')
        query = query.filter_by(status=AppointmentStatus(status))
    
    if request.args.get('type'):
        appointment_type = request.args.get('type')
        query = query.filter_by(appointment_type=AppointmentType(appointment_type))
    
    if request.args.get('date_from'):
        date_from = datetime.strptime(request.args.get('date_from'), '%Y-%m-%d')
        query = query.filter(Appointment.scheduled_date >= date_from)
    
    if request.args.get('date_to'):
        date_to = datetime.strptime(request.args.get('date_to'), '%Y-%m-%d')
        date_to = date_to.replace(hour=23, minute=59, second=59)
        query = query.filter(Appointment.scheduled_date <= date_to)
    
    # Order by scheduled date
    appointments_list = query.order_by(Appointment.scheduled_date.asc()).all()
    
    # Get statistics
    total_appointments = Appointment.query.filter_by(user_id=current_user.id).count()
    upcoming_appointments = Appointment.query.filter(
        and_(Appointment.user_id == current_user.id,
             Appointment.scheduled_date > datetime.utcnow(),
             Appointment.status.in_([AppointmentStatus.SCHEDULED, AppointmentStatus.CONFIRMED]))
    ).count()
    
    today_appointments = Appointment.query.filter(
        and_(Appointment.user_id == current_user.id,
             func.date(Appointment.scheduled_date) == datetime.utcnow().date())
    ).count()
    
    stats = {
        'total': total_appointments,
        'upcoming': upcoming_appointments,
        'today': today_appointments,
        'completed': Appointment.query.filter_by(user_id=current_user.id, status=AppointmentStatus.COMPLETED).count()
    }
    
    return render_template('appointments/index.html', 
                         appointments=appointments_list,
                         search_form=search_form,
                         stats=stats)

@appointments.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """Create a new appointment"""
    form = AppointmentForm()
    
    # Pre-populate with lead data if lead_id is provided
    lead_id = request.args.get('lead_id')
    lead = None
    if lead_id:
        lead = Lead.query.filter_by(public_id=lead_id).first()
        if lead and form.validate_on_submit():
            form.client_name.data = f"{lead.first_name} {lead.last_name}"
            form.client_email.data = lead.email
            form.client_phone.data = lead.phone
            form.client_company.data = lead.company
    
    if form.validate_on_submit():
        appointment = Appointment(
            title=form.title.data,
            description=form.description.data,
            appointment_type=AppointmentType(form.appointment_type.data),
            scheduled_date=form.scheduled_date.data,
            duration_minutes=form.duration_minutes.data,
            timezone=form.timezone.data,
            client_name=form.client_name.data,
            client_email=form.client_email.data,
            client_phone=form.client_phone.data,
            client_company=form.client_company.data,
            meeting_location=form.meeting_location.data,
            meeting_link=form.meeting_link.data,
            notes=form.notes.data,
            user_id=current_user.id,
            lead_id=lead.id if lead else None
        )
        
        db.session.add(appointment)
        db.session.commit()
        
        # Create history record
        history = AppointmentHistory(
            action=AppointmentHistoryAction.CREATED,
            details=f"Appointment created by {current_user.username}",
            appointment_id=appointment.id,
            user_id=current_user.id
        )
        db.session.add(history)
        db.session.commit()
        
        # Send confirmation email
        send_appointment_email(appointment, 'confirmation')
        
        flash('Appointment created successfully!', 'success')
        return redirect(url_for('appointments.view', public_id=appointment.public_id))
    
    return render_template('appointments/create.html', form=form, lead=lead)

@appointments.route('/<public_id>')
@login_required
def view(public_id):
    """View appointment details"""
    appointment = Appointment.query.filter_by(public_id=public_id).first_or_404()
    
    # Check if user owns this appointment
    if appointment.user_id != current_user.id:
        abort(403)
    
    # Get appointment history
    history = AppointmentHistory.query.filter_by(appointment_id=appointment.id)\
                                    .order_by(AppointmentHistory.created_at.desc()).all()
    
    return render_template('appointments/view.html', appointment=appointment, history=history)

@appointments.route('/<public_id>/update', methods=['GET', 'POST'])
@login_required
def update(public_id):
    """Update appointment details"""
    appointment = Appointment.query.filter_by(public_id=public_id).first_or_404()
    
    if appointment.user_id != current_user.id:
        abort(403)
    
    form = AppointmentUpdateForm(obj=appointment)
    
    if form.validate_on_submit():
        # Store old values for history
        old_values = {
            'title': appointment.title,
            'status': appointment.status.value,
            'scheduled_date': appointment.scheduled_date.isoformat(),
            'client_name': appointment.client_name,
            'client_email': appointment.client_email
        }
        
        # Update appointment
        form.populate_obj(appointment)
        appointment.status = AppointmentStatus(form.status.data)
        appointment.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        # Create history record
        new_values = {
            'title': appointment.title,
            'status': appointment.status.value,
            'scheduled_date': appointment.scheduled_date.isoformat(),
            'client_name': appointment.client_name,
            'client_email': appointment.client_email
        }
        
        history = AppointmentHistory(
            action=AppointmentHistoryAction.UPDATED,
            details=f"Appointment updated by {current_user.username}",
            old_values=json.dumps(old_values),
            new_values=json.dumps(new_values),
            appointment_id=appointment.id,
            user_id=current_user.id
        )
        db.session.add(history)
        db.session.commit()
        
        # Send notification email if requested
        if form.send_notification.data:
            send_appointment_email(appointment, 'update')
        
        flash('Appointment updated successfully!', 'success')
        return redirect(url_for('appointments.view', public_id=appointment.public_id))
    
    return render_template('appointments/update.html', form=form, appointment=appointment)

@appointments.route('/<public_id>/reschedule', methods=['GET', 'POST'])
@login_required
def reschedule(public_id):
    """Reschedule an appointment"""
    appointment = Appointment.query.filter_by(public_id=public_id).first_or_404()
    
    if appointment.user_id != current_user.id:
        abort(403)
    
    form = AppointmentRescheduleForm()
    
    # Pre-populate form with current values
    if request.method == 'GET':
        form.new_scheduled_date.data = appointment.scheduled_date
        form.new_duration_minutes.data = appointment.duration_minutes
    
    if form.validate_on_submit():
        # Store old values
        old_date = appointment.scheduled_date
        old_duration = appointment.duration_minutes
        
        # Update appointment
        appointment.scheduled_date = form.new_scheduled_date.data
        appointment.duration_minutes = form.new_duration_minutes.data
        appointment.status = AppointmentStatus.RESCHEDULED
        appointment.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        # Create history record
        history = AppointmentHistory(
            action=AppointmentHistoryAction.RESCHEDULED,
            details=f"Appointment rescheduled by {current_user.username}. Reason: {form.reason.data}",
            old_values=json.dumps({
                'scheduled_date': old_date.isoformat(),
                'duration_minutes': old_duration
            }),
            new_values=json.dumps({
                'scheduled_date': appointment.scheduled_date.isoformat(),
                'duration_minutes': appointment.duration_minutes
            }),
            appointment_id=appointment.id,
            user_id=current_user.id
        )
        db.session.add(history)
        db.session.commit()
        
        # Send notification email if requested
        if form.send_notification.data:
            send_appointment_email(appointment, 'reschedule', {'reason': form.reason.data})
        
        flash('Appointment rescheduled successfully!', 'success')
        return redirect(url_for('appointments.view', public_id=appointment.public_id))
    
    return render_template('appointments/reschedule.html', form=form, appointment=appointment)

@appointments.route('/<public_id>/cancel', methods=['GET', 'POST'])
@login_required
def cancel(public_id):
    """Cancel an appointment"""
    appointment = Appointment.query.filter_by(public_id=public_id).first_or_404()
    
    if appointment.user_id != current_user.id:
        abort(403)
    
    form = AppointmentCancelForm()
    
    if form.validate_on_submit():
        appointment.status = AppointmentStatus.CANCELLED
        appointment.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        # Create history record
        history = AppointmentHistory(
            action=AppointmentHistoryAction.CANCELLED,
            details=f"Appointment cancelled by {current_user.username}. Reason: {form.reason.data}",
            appointment_id=appointment.id,
            user_id=current_user.id
        )
        db.session.add(history)
        db.session.commit()
        
        # Send notification email if requested
        if form.send_notification.data:
            send_appointment_email(appointment, 'cancellation', {'reason': form.reason.data})
        
        flash('Appointment cancelled successfully!', 'warning')
        return redirect(url_for('appointments.index'))
    
    return render_template('appointments/cancel.html', form=form, appointment=appointment)

@appointments.route('/export')
@login_required
def export():
    """Export appointments to Excel"""
    appointments_list = Appointment.query.filter_by(user_id=current_user.id)\
                                        .order_by(Appointment.scheduled_date.desc()).all()
    
    # Create DataFrame
    data = []
    for appointment in appointments_list:
        data.append({
            'ID': appointment.public_id,
            'Title': appointment.title,
            'Type': appointment.appointment_type.value.replace('_', ' ').title(),
            'Status': appointment.status.value.replace('_', ' ').title(),
            'Client Name': appointment.client_name,
            'Client Email': appointment.client_email,
            'Client Phone': appointment.client_phone or '',
            'Client Company': appointment.client_company or '',
            'Scheduled Date': appointment.scheduled_date.strftime('%Y-%m-%d %H:%M'),
            'Duration (mins)': appointment.duration_minutes,
            'Location': appointment.meeting_location or '',
            'Meeting Link': appointment.meeting_link or '',
            'Notes': appointment.notes or '',
            'Created At': appointment.created_at.strftime('%Y-%m-%d %H:%M'),
            'Updated At': appointment.updated_at.strftime('%Y-%m-%d %H:%M')
        })
    
    df = pd.DataFrame(data)
    
    # Create Excel file in memory
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Appointments', index=False)
    
    output.seek(0)
    
    filename = f"appointments_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    
    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name=filename
    )

@appointments.route('/api/calendar')
@login_required
def calendar_api():
    """API endpoint for calendar view"""
    appointments_list = Appointment.query.filter_by(user_id=current_user.id)\
                                        .filter(Appointment.status != AppointmentStatus.CANCELLED)\
                                        .all()
    
    events = []
    for appointment in appointments_list:
        end_time = appointment.scheduled_date + timedelta(minutes=appointment.duration_minutes)
        
        events.append({
            'id': appointment.public_id,
            'title': appointment.title,
            'start': appointment.scheduled_date.isoformat(),
            'end': end_time.isoformat(),
            'description': f"{appointment.client_name} - {appointment.appointment_type.value}",
            'status': appointment.status.value,
            'url': url_for('appointments.view', public_id=appointment.public_id)
        })
    
    return jsonify(events)

def send_appointment_email(appointment, email_type, extra_data=None):
    """Send appointment-related emails"""
    try:
        subject_templates = {
            'confirmation': f"Appointment Confirmation - {appointment.title}",
            'update': f"Appointment Updated - {appointment.title}",
            'reschedule': f"Appointment Rescheduled - {appointment.title}",
            'cancellation': f"Appointment Cancelled - {appointment.title}",
            'reminder': f"Appointment Reminder - {appointment.title}"
        }
        
        subject = subject_templates.get(email_type, f"Appointment Notification - {appointment.title}")
        
        # Create email body based on type
        if email_type == 'confirmation':
            body = f"""
            Dear {appointment.client_name},
            
            Your appointment has been confirmed with the following details:
            
            Title: {appointment.title}
            Date & Time: {appointment.scheduled_date.strftime('%Y-%m-%d at %H:%M')} ({appointment.timezone})
            Duration: {appointment.duration_minutes} minutes
            Type: {appointment.appointment_type.value.replace('_', ' ').title()}
            
            """
        elif email_type == 'reschedule':
            reason = extra_data.get('reason', '') if extra_data else ''
            body = f"""
            Dear {appointment.client_name},
            
            Your appointment has been rescheduled:
            
            Title: {appointment.title}
            New Date & Time: {appointment.scheduled_date.strftime('%Y-%m-%d at %H:%M')} ({appointment.timezone})
            Duration: {appointment.duration_minutes} minutes
            
            Reason: {reason}
            """
        elif email_type == 'cancellation':
            reason = extra_data.get('reason', '') if extra_data else ''
            body = f"""
            Dear {appointment.client_name},
            
            Unfortunately, your appointment has been cancelled:
            
            Title: {appointment.title}
            Original Date & Time: {appointment.scheduled_date.strftime('%Y-%m-%d at %H:%M')}
            
            Reason: {reason}
            
            Please contact us to reschedule if needed.
            """
        else:
            body = f"""
            Dear {appointment.client_name},
            
            This is an update regarding your appointment:
            
            Title: {appointment.title}
            Date & Time: {appointment.scheduled_date.strftime('%Y-%m-%d at %H:%M')} ({appointment.timezone})
            Status: {appointment.status.value.replace('_', ' ').title()}
            """
        
        # Add common footer
        if appointment.meeting_location:
            body += f"\nLocation: {appointment.meeting_location}"
        if appointment.meeting_link:
            body += f"\nMeeting Link: {appointment.meeting_link}"
        if appointment.notes:
            body += f"\nNotes: {appointment.notes}"
        
        body += f"\n\nBest regards,\n{current_user.username}"
        
        # Send email
        msg = Message(
            subject=subject,
            recipients=[appointment.client_email],
            body=body
        )
        
        mail.send(msg)
        
        # Create history record for email sent
        history = AppointmentHistory(
            action=AppointmentHistoryAction.EMAIL_SENT,
            details=f"{email_type.title()} email sent to {appointment.client_email}",
            appointment_id=appointment.id,
            user_id=current_user.id
        )
        db.session.add(history)
        db.session.commit()
        
        return True
        
    except Exception as e:
        current_app.logger.error(f"Failed to send appointment email: {str(e)}")
        return False