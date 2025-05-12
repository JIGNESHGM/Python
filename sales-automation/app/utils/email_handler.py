from flask import current_app, render_template
from flask_mail import Message
from app import mail
from datetime import datetime
import time
import random
from app.models import Campaign

class EmailAutomation:
    def __init__(self):
        self.tracking_base_url = current_app.config.get('TRACKING_BASE_URL', 'http://localhost:5000')
        
    def create_email(self, lead, template_name='email_template.html'):
        """Create personalized email message"""
        # Create campaign record first to get tracking token
        campaign_id, tracking_token = Campaign.create(lead['_id'])
        
        email_html = render_template(
            template_name,
            recipient_name=lead.get('contact_person', 'Sir/Madam'),
            company_name=lead.get('company_name', ''),
            tracking_token=tracking_token,
            tracking_base_url=self.tracking_base_url
        )
        
        subject = f"Custom solution for {lead.get('company_name', 'your company')}"
        
        msg = Message(
            subject=subject,
            recipients=[lead.get('email')],
            html=email_html,
            sender=current_app.config['MAIL_USERNAME']
        )
        
        return msg, campaign_id
    
    def send_email_campaign(self, leads, batch_size=10, delay=30):
        """Send email campaign in batches"""
        sent_count = 0
        failed_count = 0
        
        for i, lead in enumerate(leads):
            try:
                if not lead.get('email'):
                    continue
                    
                msg, campaign_id = self.create_email(lead)
                
                # Send email
                mail.send(msg)
                
                # Update campaign as sent
                Campaign.update(campaign_id, {
                    'email_sent': True,
                    'sent_at': datetime.utcnow()
                })
                
                sent_count += 1
                
                # Batch control
                if (i + 1) % batch_size == 0:
                    time.sleep(delay)
                    
            except Exception as e:
                print(f"Failed to send to {lead.get('email')}: {str(e)}")
                failed_count += 1
                continue
                
        return {
            'total': len(leads),
            'sent': sent_count,
            'failed': failed_count
        }