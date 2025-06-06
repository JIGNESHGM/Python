from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, current_app, send_from_directory, abort
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app import db, mail
from app.models import User, Lead, Campaign, EmailTemplate, LeadInteraction, SentEmail, CampaignStatus, LeadStatus, LeadInteractionType, SentEmailStatus
from app.forms import (LoginForm, RegistrationForm, CampaignForm, LeadForm, 
                      EmailTemplateForm, UploadLeadsForm, CampaignSettingsForm)
from app.utils.scraping import run_scraping_job, validate_scraping_config
from app.utils.email_handler import send_test_email, queue_campaign_emails
from app.utils.analytics import generate_analytics_report
import pandas as pd
import os
from datetime import datetime, timedelta
from sqlalchemy import func
import uuid
import json

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    # Dashboard statistics
    total_leads = Lead.query.count()
    total_campaigns = Campaign.query.count()
    active_campaigns = Campaign.query.filter_by(status=CampaignStatus.ACTIVE).count()
    
    # Recent leads
    recent_leads = Lead.query.order_by(Lead.created_at.desc()).limit(5).all()
    
    # Campaign performance
    campaigns = Campaign.query.all()
    
    return render_template('index.html', 
                         total_leads=total_leads,
                         total_campaigns=total_campaigns,
                         active_campaigns=active_campaigns,
                         recent_leads=recent_leads,
                         campaigns=campaigns)

@main.route('/leads')
@login_required
def leads():
    page = request.args.get('page', 1, type=int)
    status_filter = request.args.get('status', 'all')
    search_query = request.args.get('q', '')
    
    query = Lead.query
    
    if status_filter != 'all':
        query = query.filter_by(status=LeadStatus[status_filter.upper()])
    
    if search_query:
        search = f"%{search_query}%"
        query = query.filter(
            (Lead.first_name.ilike(search)) | 
            (Lead.last_name.ilike(search)) |
            (Lead.company.ilike(search)) |
            (Lead.email.ilike(search))
    
    leads = query.order_by(Lead.created_at.desc()).paginate(page=page, per_page=20)
    
    return render_template('leads.html', leads=leads, status_filter=status_filter, search_query=search_query)

@main.route('/leads/<public_id>')
@login_required
def lead_detail(public_id):
    lead = Lead.query.filter_by(public_id=public_id).first_or_404()
    interactions = lead.interactions.order_by(LeadInteraction.created_at.desc()).all()
    return render_template('lead_detail.html', lead=lead, interactions=interactions)

@main.route('/leads/add', methods=['GET', 'POST'])
@login_required
def add_lead():
    form = LeadForm()
    if form.validate_on_submit():
        lead = Lead(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            company=form.company.data,
            position=form.position.data,
            industry=form.industry.data,
            website=form.website.data,
            location=form.location.data,
            notes=form.notes.data,
            source='manual_entry'
        )
        db.session.add(lead)
        db.session.commit()
        flash('Lead added successfully!', 'success')
        return redirect(url_for('main.leads'))
    return render_template('add_lead.html', form=form)

@main.route('/leads/import', methods=['GET', 'POST'])
@login_required
def import_leads():
    form = UploadLeadsForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Read the file based on extension
            if filename.endswith('.csv'):
                df = pd.read_csv(filepath)
            elif filename.endswith('.xlsx'):
                df = pd.read_excel(filepath)
            else:
                flash('Unsupported file format', 'danger')
                return redirect(url_for('main.import_leads'))
            
            # Process the DataFrame
            required_columns = {'email', 'first_name', 'last_name', 'company'}
            if not required_columns.issubset(df.columns):
                missing = required_columns - set(df.columns)
                flash(f'Missing required columns: {", ".join(missing)}', 'danger')
                return redirect(url_for('main.import_leads'))
            
            # Import leads
            imported = 0
            for _, row in df.iterrows():
                # Check if lead already exists
                if not Lead.query.filter_by(email=row['email']).first():
                    lead = Lead(
                        first_name=row.get('first_name', ''),
                        last_name=row.get('last_name', ''),
                        email=row['email'],
                        phone=row.get('phone', ''),
                        company=row.get('company', ''),
                        position=row.get('position', ''),
                        industry=row.get('industry', ''),
                        website=row.get('website', ''),
                        location=row.get('location', ''),
                        notes=row.get('notes', ''),
                        source='import'
                    )
                    db.session.add(lead)
                    imported += 1
            
            db.session.commit()
            flash(f'Successfully imported {imported} leads', 'success')
            return redirect(url_for('main.leads'))
        
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Error importing leads: {str(e)}")
            flash('Error importing leads. Please check the file format.', 'danger')
        
        finally:
            # Clean up the uploaded file
            if os.path.exists(filepath):
                os.remove(filepath)
    
    return render_template('import_leads.html', form=form)

@main.route('/campaigns')
@login_required
def campaigns():
    status_filter = request.args.get('status', 'all')
    
    query = Campaign.query
    
    if status_filter != 'all':
        query = query.filter_by(status=CampaignStatus[status_filter.upper()])
    
    campaigns = query.order_by(Campaign.created_at.desc()).all()
    return render_template('campaigns.html', campaigns=campaigns, status_filter=status_filter)

@main.route('/campaigns/create', methods=['GET', 'POST'])
@login_required
def create_campaign():
    form = CampaignForm()
    if form.validate_on_submit():
        campaign = Campaign(
            name=form.name.data,
            description=form.description.data,
            status=CampaignStatus.DRAFT,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            user_id=current_user.id
        )
        db.session.add(campaign)
        db.session.commit()
        
        # Create analytics entry
        analytics = CampaignAnalytics(campaign_id=campaign.id)
        db.session.add(analytics)
        db.session.commit()
        
        flash('Campaign created successfully!', 'success')
        return redirect(url_for('main.campaign_detail', public_id=campaign.public_id))
    return render_template('create_campaign.html', form=form)

@main.route('/campaigns/<public_id>')
@login_required
def campaign_detail(public_id):
    campaign = Campaign.query.filter_by(public_id=public_id).first_or_404()
    
    # Statistics
    leads_count = campaign.leads.count()
    emails_sent = SentEmail.query.filter_by(campaign_id=campaign.id).count()
    emails_opened = SentEmail.query.filter(SentEmail.campaign_id==campaign.id, SentEmail.open_count>0).count()
    replies_received = db.session.query(func.count(LeadInteraction.id)).filter(
        LeadInteraction.campaign_id==campaign.id,
        LeadInteraction.interaction_type==LeadInteractionType.REPLY_RECEIVED
    ).scalar()
    
    # Lead status distribution
    status_distribution = db.session.query(
        Lead.status,
        func.count(Lead.id)
    ).filter(Lead.campaign_id==campaign.id).group_by(Lead.status).all()
    
    return render_template('campaign_detail.html', 
                        campaign=campaign,
                        leads_count=leads_count,
                        emails_sent=emails_sent,
                        emails_opened=emails_opened,
                        replies_received=replies_received,
                        status_distribution=status_distribution)

@main.route('/campaigns/<public_id>/settings', methods=['GET', 'POST'])
@login_required
def campaign_settings(public_id):
    campaign = Campaign.query.filter_by(public_id=public_id).first_or_404()
    form = CampaignSettingsForm(obj=campaign)
    
    if form.validate_on_submit():
        campaign.name = form.name.data
        campaign.description = form.description.data
        campaign.status = CampaignStatus[form.status.data]
        campaign.start_date = form.start_date.data
        campaign.end_date = form.end_date.data
        db.session.commit()
        flash('Campaign settings updated!', 'success')
        return redirect(url_for('main.campaign_detail', public_id=campaign.public_id))
    
    return render_template('campaign_settings.html', campaign=campaign, form=form)

@main.route('/campaigns/<public_id>/leads')
@login_required
def campaign_leads(public_id):
    campaign = Campaign.query.filter_by(public_id=public_id).first_or_404()
    page = request.args.get('page', 1, type=int)
    status_filter = request.args.get('status', 'all')
    
    query = campaign.leads
    
    if status_filter != 'all':
        query = query.filter_by(status=LeadStatus[status_filter.upper()])
    
    leads = query.order_by(Lead.created_at.desc()).paginate(page=page, per_page=20)
    
    return render_template('campaign_leads.html', 
                         campaign=campaign, 
                         leads=leads, 
                         status_filter=status_filter)

@main.route('/campaigns/<public_id>/leads/add', methods=['GET', 'POST'])
@login_required
def campaign_add_lead(public_id):
    campaign = Campaign.query.filter_by(public_id=public_id).first_or_404()
    form = LeadForm()
    
    if form.validate_on_submit():
        lead = Lead(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            company=form.company.data,
            position=form.position.data,
            industry=form.industry.data,
            website=form.website.data,
            location=form.location.data,
            notes=form.notes.data,
            source='manual_entry',
            campaign_id=campaign.id
        )
        db.session.add(lead)
        db.session.commit()
        flash('Lead added to campaign successfully!', 'success')
        return redirect(url_for('main.campaign_leads', public_id=campaign.public_id))
    
    return render_template('campaign_add_lead.html', campaign=campaign, form=form)

@main.route('/campaigns/<public_id>/leads/import', methods=['GET', 'POST'])
@login_required
def campaign_import_leads(public_id):
    campaign = Campaign.query.filter_by(public_id=public_id).first_or_404()
    form = UploadLeadsForm()
    
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Read the file based on extension
            if filename.endswith('.csv'):
                df = pd.read_csv(filepath)
            elif filename.endswith('.xlsx'):
                df = pd.read_excel(filepath)
            else:
                flash('Unsupported file format', 'danger')
                return redirect(url_for('main.campaign_import_leads', public_id=public_id))
            
            # Process the DataFrame
            required_columns = {'email', 'first_name', 'last_name', 'company'}
            if not required_columns.issubset(df.columns):
                missing = required_columns - set(df.columns)
                flash(f'Missing required columns: {", ".join(missing)}', 'danger')
                return redirect(url_for('main.campaign_import_leads', public_id=public_id))
            
            # Import leads
            imported = 0
            for _, row in df.iterrows():
                # Check if lead already exists in this campaign
                if not Lead.query.filter_by(email=row['email'], campaign_id=campaign.id).first():
                    lead = Lead(
                        first_name=row.get('first_name', ''),
                        last_name=row.get('last_name', ''),
                        email=row['email'],
                        phone=row.get('phone', ''),
                        company=row.get('company', ''),
                        position=row.get('position', ''),
                        industry=row.get('industry', ''),
                        website=row.get('website', ''),
                        location=row.get('location', ''),
                        notes=row.get('notes', ''),
                        source='import',
                        campaign_id=campaign.id
                    )
                    db.session.add(lead)
                    imported += 1
            
            db.session.commit()
            flash(f'Successfully imported {imported} leads to campaign', 'success')
            return redirect(url_for('main.campaign_leads', public_id=public_id))
        
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Error importing leads: {str(e)}")
            flash('Error importing leads. Please check the file format.', 'danger')
        
        finally:
            # Clean up the uploaded file
            if os.path.exists(filepath):
                os.remove(filepath)
    
    return render_template('campaign_import_leads.html', campaign=campaign, form=form)

@main.route('/campaigns/<public_id>/templates')
@login_required
def campaign_templates(public_id):
    campaign = Campaign.query.filter_by(public_id=public_id).first_or_404()
    templates = campaign.emails.all()
    return render_template('campaign_templates.html', campaign=campaign, templates=templates)

@main.route('/campaigns/<public_id>/templates/create', methods=['GET', 'POST'])
@login_required
def create_template(public_id):
    campaign = Campaign.query.filter_by(public_id=public_id).first_or_404()
    form = EmailTemplateForm()
    
    if form.validate_on_submit():
        template = EmailTemplate(
            name=form.name.data,
            subject=form.subject.data,
            body=form.body.data,
            is_html=form.is_html.data,
            campaign_id=campaign.id
        )
        db.session.add(template)
        db.session.commit()
        flash('Email template created successfully!', 'success')
        return redirect(url_for('main.campaign_templates', public_id=campaign.public_id))
    
    return render_template('create_template.html', campaign=campaign, form=form)

@main.route('/templates/<public_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_template(public_id):
    template = EmailTemplate.query.filter_by(public_id=public_id).first_or_404()
    form = EmailTemplateForm(obj=template)
    
    if form.validate_on_submit():
        template.name = form.name.data
        template.subject = form.subject.data
        template.body = form.body.data
        template.is_html = form.is_html.data
        db.session.commit()
        flash('Email template updated successfully!', 'success')
        return redirect(url_for('main.campaign_templates', public_id=template.campaign.public_id))
    
    return render_template('edit_template.html', template=template, form=form)

@main.route('/templates/<public_id>/preview')
@login_required
def preview_template(public_id):
    template = EmailTemplate.query.filter_by(public_id=public_id).first_or_404()
    return render_template('email_preview.html', template=template)

@main.route('/templates/<public_id>/test', methods=['GET', 'POST'])
@login_required
def test_template(public_id):
    template = EmailTemplate.query.filter_by(public_id=public_id).first_or_404()
    
    if request.method == 'POST':
        test_email = request.form.get('test_email')
        if test_email:
            # Create a test lead
            test_lead = Lead(
                first_name="Test",
                last_name="User",
                email=test_email,
                company="Test Company",
                campaign_id=template.campaign_id
            )
            
            # Send test email
            success = send_test_email(template, test_lead, test_email)
            if success:
                flash('Test email sent successfully!', 'success')
            else:
                flash('Failed to send test email', 'danger')
            
            return redirect(url_for('main.test_template', public_id=public_id))
    
    return render_template('test_template.html', template=template)

@main.route('/campaigns/<public_id>/send', methods=['GET', 'POST'])
@login_required
def send_campaign(public_id):
    campaign = Campaign.query.filter_by(public_id=public_id).first_or_404()
    
    if request.method == 'POST':
        template_id = request.form.get('template_id')
        if not template_id:
            flash('Please select an email template', 'danger')
            return redirect(url_for('main.send_campaign', public_id=public_id))
        
        template = EmailTemplate.query.get(template_id)
        if not template:
            flash('Invalid email template', 'danger')
            return redirect(url_for('main.send_campaign', public_id=public_id))
        
        # Queue emails for sending
        queue_campaign_emails(campaign, template)
        flash('Emails have been queued for sending!', 'success')
        return redirect(url_for('main.campaign_detail', public_id=public_id))
    
    # Get available templates
    templates = campaign.emails.all()
    return render_template('send_campaign.html', campaign=campaign, templates=templates)

@main.route('/scrape', methods=['GET', 'POST'])
@login_required
def scrape():
    if request.method == 'POST':
        # Get scraping configuration from form
        config = {
            'source': request.form.get('source'),
            'query': request.form.get('query'),
            'max_results': int(request.form.get('max_results', 50)),
            'filters': {
                'industry': request.form.get('industry'),
                'location': request.form.get('location'),
                'company_size': request.form.get('company_size')
            }
        }
        
        # Validate config
        if not validate_scraping_config(config):
            flash('Invalid scraping configuration', 'danger')
            return redirect(url_for('main.scrape'))
        
        # Run scraping job in background
        try:
            results = run_scraping_job(config)
            flash(f'Successfully scraped {len(results)} leads', 'success')
            return redirect(url_for('main.scrape_results', job_id='latest'))
        except Exception as e:
            current_app.logger.error(f"Scraping error: {str(e)}")
            flash('Error during scraping. Please try again.', 'danger')
    
    return render_template('scrape.html')

@main.route('/scrape/results/<job_id>')
@login_required
def scrape_results(job_id):
    # In a real app, you'd fetch results from a database or cache
    # For this example, we'll just return a placeholder
    return render_template('scrape_results.html')

@main.route('/analytics')
@login_required
def analytics():
    # Overall statistics
    total_leads = Lead.query.count()
    total_campaigns = Campaign.query.count()
    total_emails_sent = SentEmail.query.count()
    
    # Campaign performance
    campaigns = Campaign.query.all()
    campaign_data = []
    
    for campaign in campaigns:
        analytics = campaign.analytics
        campaign_data.append({
            'name': campaign.name,
            'emails_sent': analytics.emails_sent,
            'open_rate': analytics.open_rate,
            'click_rate': analytics.click_rate,
            'replies_received': analytics.replies_received
        })
    
    # Lead source distribution
    lead_sources = db.session.query(
        Lead.source,
        func.count(Lead.id).label('count')
    ).group_by(Lead.source).all()
    
    # Generate report
    report = generate_analytics_report()
    
    return render_template('analytics.html',
                        total_leads=total_leads,
                        total_campaigns=total_campaigns,
                        total_emails_sent=total_emails_sent,
                        campaign_data=campaign_data,
                        lead_sources=lead_sources,
                        report=report)

@main.route('/track/open/<public_id>')
def track_open(public_id):
    email = SentEmail.query.filter_by(public_id=public_id).first()
    if email:
        # Update open count and timestamp
        email.open_count += 1
        if not email.opened_at:
            email.opened_at = datetime.utcnow()
        db.session.commit()
        
        # Record interaction
        interaction = LeadInteraction(
            interaction_type=LeadInteractionType.EMAIL_OPENED,
            lead_id=email.lead_id,
            email_id=email.id,
            details=f"Email opened at {datetime.utcnow()}"
        )
        db.session.add(interaction)
        db.session.commit()
        
        # Update campaign analytics
        if email.campaign_id:
            campaign = Campaign.query.get(email.campaign_id)
            if campaign and campaign.analytics:
                campaign.analytics.update_metrics()
    
    # Return transparent pixel
    return send_from_directory(current_app.static_folder, 'images/pixel.png')

@main.route('/track/click/<public_id>')
def track_click(public_id):
    email = SentEmail.query.filter_by(public_id=public_id).first()
    if email:
        # Record interaction
        interaction = LeadInteraction(
            interaction_type=LeadInteractionType.LINK_CLICKED,
            lead_id=email.lead_id,
            email_id=email.id,
            details=f"Link clicked at {datetime.utcnow()}"
        )
        db.session.add(interaction)
        db.session.commit()
        
        # Update campaign analytics
        if email.campaign_id:
            campaign = Campaign.query.get(email.campaign_id)
            if campaign and campaign.analytics:
                campaign.analytics.update_metrics()
    
    # Redirect to actual URL (would be stored in a separate table in a real app)
    return redirect('https://yourcompany.com')

@main.route('/api/leads/chart')
@login_required
def leads_chart_data():
    # Generate data for leads over time chart
    data = db.session.query(
        func.date(Lead.created_at).label('date'),
        func.count(Lead.id).label('count')
    ).group_by(func.date(Lead.created_at)).order_by(func.date(Lead.created_at)).all()
    
    return jsonify({
        'dates': [d.date.isoformat() for d in data],
        'counts': [d.count for d in data]
    })

@main.route('/api/campaigns/performance')
@login_required
def campaigns_performance_data():
    campaigns = Campaign.query.all()
    data = []
    
    for campaign in campaigns:
        analytics = campaign.analytics
        data.append({
            'name': campaign.name,
            'emails_sent': analytics.emails_sent,
            'open_rate': analytics.open_rate,
            'click_rate': analytics.click_rate,
            'replies': analytics.replies_received
        })
    
    return jsonify(data)