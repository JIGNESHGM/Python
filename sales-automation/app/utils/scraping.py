from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SelectField, DateField, FileField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models import User, Campaign
from datetime import datetime

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', 
                                   validators=[DataRequired(), EqualTo('password')])
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already registered.')

class CampaignForm(FlaskForm):
    name = StringField('Campaign Name', validators=[DataRequired(), Length(max=120)])
    description = TextAreaField('Description')
    start_date = DateField('Start Date', format='%Y-%m-%d', default=datetime.utcnow)
    end_date = DateField('End Date', format='%Y-%m-%d')

    def validate_end_date(self, end_date):
        if end_date.data and self.start_date.data:
            if end_date.data < self.start_date.data:
                raise ValidationError('End date must be after start date.')

class CampaignSettingsForm(CampaignForm):
    status = SelectField('Status', choices=[
        ('DRAFT', 'Draft'),
        ('ACTIVE', 'Active'),
        ('PAUSED', 'Paused'),
        ('COMPLETED', 'Completed')
    ])

class LeadForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=64)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    phone = StringField('Phone', validators=[Length(max=20)])
    company = StringField('Company', validators=[DataRequired(), Length(max=120)])
    position = StringField('Position', validators=[Length(max=120)])
    industry = StringField('Industry', validators=[Length(max=120)])
    website = StringField('Website', validators=[Length(max=256)])
    location = StringField('Location', validators=[Length(max=120)])
    notes = TextAreaField('Notes')

class EmailTemplateForm(FlaskForm):
    name = StringField('Template Name', validators=[DataRequired(), Length(max=120)])
    subject = StringField('Subject', validators=[DataRequired(), Length(max=256)])
    body = TextAreaField('Body', validators=[DataRequired()])
    is_html = BooleanField('HTML Email', default=True)

class UploadLeadsForm(FlaskForm):
    file = FileField('Leads File (CSV or Excel)', validators=[DataRequired()])