from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ScrapeForm(FlaskForm):
    search_query = StringField('Search Query', validators=[DataRequired()])
    data_source = SelectField('Data Source', choices=[
        ('google', 'Google'),
        ('linkedin', 'LinkedIn')
    ], validators=[DataRequired()])
    pages = IntegerField('Number of Pages', default=1, validators=[
        NumberRange(min=1, max=10)
    ])
    export_excel = BooleanField('Export to Excel')
    submit = SubmitField('Scrape Data')

class CampaignForm(FlaskForm):
    leads = SelectMultipleField('Select Leads', coerce=str)
    batch_size = IntegerField('Emails per Batch', default=10, validators=[
        NumberRange(min=1, max=50)
    ])
    delay = IntegerField('Delay Between Batches (seconds)', default=30, validators=[
        NumberRange(min=5, max=300)
    ])
    submit = SubmitField('Start Campaign')