from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file
from flask import current_app, make_response
from app.forms import ScrapeForm, CampaignForm
from app.utils.scraping import WebScraper
from app.utils.email_handler import EmailAutomation
from app.utils.nlp_processor import LeadScorer
from app.models import Lead, Campaign
from io import BytesIO
import pandas as pd
from datetime import datetime
import uuid

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/scrape', methods=['GET', 'POST'])
def scrape():
    form = ScrapeForm()
    if form.validate_on_submit():
        scraper = WebScraper()
        query = form.search_query.data
        source = form.data_source.data
        
        if source == 'google':
            results = scraper.scrape_google(query, pages=form.pages.data)
        elif source == 'linkedin':
            results = scraper.scrape_linkedin(query)
        else:
            flash('Invalid data source selected', 'danger')
            return redirect(url_for('main.scrape'))
            
        # Save to database
        for result in results:
            Lead.create(
                company_name=result.get('company_name'),
                email=result.get('email', ''),
                contact_person=result.get('contact_person', ''),
                industry=result.get('industry', ''),
                website=result.get('website', ''),
                location=result.get('location', ''),
                source=source
            )
        
        # Export to Excel if requested
        if form.export_excel.data:
            df = pd.DataFrame(results)
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='openpyxl')
            df.to_excel(writer, sheet_name='Leads', index=False)
            writer.save()
            output.seek(0)
            
            flash(f'Successfully scraped {len(results)} leads', 'success')
            return send_file(
                output,
                mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                as_attachment=True,
                download_name='leads.xlsx'
            )
            
        flash(f'Successfully scraped {len(results)} leads', 'success')
        return redirect(url_for('main.leads'))
        
    return render_template('scrape.html', form=form)

@bp.route('/leads')
def leads():
    leads = Lead.get_all()
    return render_template('leads.html', leads=leads)

@bp.route('/campaign', methods=['GET', 'POST'])
def campaign():
    form = CampaignForm()
    leads = Lead.get_all()
    form.leads.choices = [(str(lead['_id']), f"{lead.get('company_name', 'No name')} - {lead.get('email', 'No email')}"] for lead in leads if lead.get('email')]
    
    if form.validate_on_submit():
        selected_lead_ids = form.leads.data
        selected_leads = [lead for lead in leads if str(lead['_id']) in selected_lead_ids]
        
        emailer = EmailAutomation()
        result = emailer.send_email_campaign(
            selected_leads,
            batch_size=form.batch_size.data,
            delay=form.delay.data
        )
        
        flash(f"Campaign sent: {result['sent']} emails, {result['failed']} failed", 'success')
        return redirect(url_for('main.analytics'))
        
    return render_template('campaign.html', form=form)

@bp.route('/analytics')
def analytics():
    lead_scorer = LeadScorer()
    lead_scorer.categorize_leads()
    
    stats = Campaign.get_analytics()
    
    # Calculate rates
    stats['open_rate'] = (stats['opened'] / stats['sent'] * 100) if stats['sent'] > 0 else 0
    stats['click_rate'] = (stats['clicked'] / stats['sent'] * 100) if stats['sent'] > 0 else 0
    stats['response_rate'] = (stats['responded'] / stats['sent'] * 100) if stats['sent'] > 0 else 0
    
    return render_template('analytics.html', stats=stats)

@bp.route('/track/<tracking_token>')
def track_email(tracking_token):
    campaign = Campaign.get_by_token(tracking_token)
    if not campaign:
        return redirect(url_for('main.index'))
    
    update_data = {}
    
    if 'pixel' in request.args:  # Email opened
        if not campaign.get('email_opened'):
            update_data['email_opened'] = True
            update_data['opened_at'] = datetime.utcnow()
            
            # Return transparent pixel
            response = make_response(
                b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'
            )
            response.headers['Content-Type'] = 'image/gif'
            response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
            
            if update_data:
                Campaign.update(campaign['_id'], update_data)
            
            return response
    else:  # Link clicked
        update_data['link_clicked'] = True
        update_data['clicked_at'] = datetime.utcnow()
        
        if update_data:
            Campaign.update(campaign['_id'], update_data)
        
        return redirect(url_for('main.index'))
    
    return redirect(url_for('main.index'))