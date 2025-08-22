from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateTimeField, IntegerField, EmailField, TelField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange
from wtforms.widgets import DateTimeLocalInput
from datetime import datetime, timedelta
from app.models import AppointmentType, AppointmentStatus

class AppointmentForm(FlaskForm):
    """Form for creating and editing appointments"""
    title = StringField('Appointment Title', validators=[DataRequired(), Length(min=3, max=200)])
    description = TextAreaField('Description', validators=[Optional(), Length(max=500)])
    appointment_type = SelectField('Appointment Type', 
                                 choices=[(t.value, t.value.replace('_', ' ').title()) for t in AppointmentType],
                                 validators=[DataRequired()])
    
    # Date and time
    scheduled_date = DateTimeField('Scheduled Date & Time', 
                                 widget=DateTimeLocalInput(),
                                 validators=[DataRequired()],
                                 format='%Y-%m-%dT%H:%M')
    duration_minutes = IntegerField('Duration (minutes)', 
                                  validators=[DataRequired(), NumberRange(min=15, max=480)],
                                  default=60)
    timezone = SelectField('Timezone', 
                         choices=[
                             ('UTC', 'UTC'),
                             ('US/Eastern', 'Eastern Time'),
                             ('US/Central', 'Central Time'),
                             ('US/Mountain', 'Mountain Time'),
                             ('US/Pacific', 'Pacific Time'),
                             ('Europe/London', 'London'),
                             ('Europe/Paris', 'Paris'),
                             ('Asia/Tokyo', 'Tokyo'),
                             ('Asia/Kolkata', 'India Standard Time')
                         ],
                         default='UTC')
    
    # Client information
    client_name = StringField('Client Name', validators=[DataRequired(), Length(min=2, max=120)])
    client_email = EmailField('Client Email', validators=[DataRequired(), Email()])
    client_phone = TelField('Client Phone', validators=[Optional(), Length(max=20)])
    client_company = StringField('Client Company', validators=[Optional(), Length(max=120)])
    
    # Meeting details
    meeting_location = StringField('Meeting Location', validators=[Optional(), Length(max=256)])
    meeting_link = StringField('Meeting Link (Zoom, Teams, etc.)', validators=[Optional(), Length(max=512)])
    notes = TextAreaField('Notes', validators=[Optional(), Length(max=1000)])
    
    submit = SubmitField('Save Appointment')

class AppointmentUpdateForm(AppointmentForm):
    """Form for updating appointment status and details"""
    status = SelectField('Status',
                        choices=[(s.value, s.value.replace('_', ' ').title()) for s in AppointmentStatus],
                        validators=[DataRequired()])
    
    send_notification = BooleanField('Send email notification to client', default=True)
    submit = SubmitField('Update Appointment')

class AppointmentRescheduleForm(FlaskForm):
    """Form for rescheduling appointments"""
    new_scheduled_date = DateTimeField('New Date & Time',
                                     widget=DateTimeLocalInput(),
                                     validators=[DataRequired()],
                                     format='%Y-%m-%dT%H:%M')
    new_duration_minutes = IntegerField('Duration (minutes)',
                                      validators=[DataRequired(), NumberRange(min=15, max=480)])
    reason = TextAreaField('Reason for Rescheduling', 
                          validators=[Optional(), Length(max=500)])
    send_notification = BooleanField('Send email notification to client', default=True)
    submit = SubmitField('Reschedule Appointment')

class AppointmentCancelForm(FlaskForm):
    """Form for cancelling appointments"""
    reason = TextAreaField('Reason for Cancellation',
                          validators=[DataRequired(), Length(min=5, max=500)])
    send_notification = BooleanField('Send email notification to client', default=True)
    submit = SubmitField('Cancel Appointment')

class AppointmentSearchForm(FlaskForm):
    """Form for searching and filtering appointments"""
    search_query = StringField('Search', validators=[Optional()])
    status_filter = SelectField('Status',
                               choices=[('', 'All Statuses')] + 
                                      [(s.value, s.value.replace('_', ' ').title()) for s in AppointmentStatus])
    type_filter = SelectField('Type',
                             choices=[('', 'All Types')] +
                                    [(t.value, t.value.replace('_', ' ').title()) for t in AppointmentType])
    date_from = DateTimeField('From Date', validators=[Optional()], format='%Y-%m-%d')
    date_to = DateTimeField('To Date', validators=[Optional()], format='%Y-%m-%d')
    submit = SubmitField('Search')

class BulkAppointmentActionForm(FlaskForm):
    """Form for bulk actions on appointments"""
    action = SelectField('Action',
                        choices=[
                            ('', 'Select Action'),
                            ('cancel', 'Cancel Selected'),
                            ('complete', 'Mark as Completed'),
                            ('send_reminder', 'Send Reminder Emails'),
                            ('export', 'Export to Excel')
                        ],
                        validators=[DataRequired()])
    reason = TextAreaField('Reason (for cancellations)', validators=[Optional()])
    submit = SubmitField('Apply Action')