import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import current_app, url_for
from app import db, mail
from app.models import SentEmail, LeadInteraction, SentEmailStatus
from datetime import datetime
import time
import threading
from queue import Queue
import logging
from config import Config
from flask_mail import Message
import html
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Email queue for background processing
email_queue = Queue()

def process_email_queue():
    """Process emails from the queue in the background"""
    while True:
        email_data = email_queue.get()
        if email_data is None:  # Sentinel value to stop the thread
            break
            
        try:
            send_email_now(**email_data)
        except Exception as e:
            logger.error(f"Error sending email: {str(e)}")
        finally:
            email_queue.task_done()

# Start email processing thread
email_thread = threading.Thread(target=process_email_queue)
email_thread.daemon = True
email_thread.start()

def personalize_email_content(template, lead):
    """Personalize email content with lead data"""
    placeholders = {
        '{first_name}': lead.first_name,
        '{last_name}': lead.last_name,
        '{full_name}': f"{lead.first_name} {lead.last_name}",
        '{company}': lead.company,
        '{industry}': lead.industry,
        '{location}': lead.location
    }
    
    subject = template.subject
    body = template.body
    
    for placeholder, value in placeholders.items():
        subject = subject.replace(placeholder, value)
        body = body.replace(placeholder, value)
    
    # Add tracking pixel and links
    if template.is_html:
        tracking_pixel = f'<img src="{url_for("main.track_open", public_id="{public_id}", _external=True)}" width="1" height="1" alt="">'
        body = body.replace('</body>', f'{tracking_pixel}</body>')
        
        # Replace links with tracking links (simplified example)
        body = re.sub(r'href="(http[^"]+)"', 
                     lambda m: f'href="{url_for("main.track_click", public_id="{public_id}", _external=True)}?redirect={m.group(1)}"', 
                     body)
    
    return subject, body

def send_test_email(template, lead, recipient_email):
    """Send a test email to verify the template"""
    try:
        subject, body = personalize_email_content(template, lead)
        
        # Create a test sent email record
        sent_email = SentEmail(
            subject=subject,
            body=body,
            recipient_email=recipient_email,
            status=SentEmailStatus.SENT,
            sent_at=datetime.utcnow(),
            template_id=template.id,
            lead_id=lead.id,
            campaign_id=template.campaign_id
        )
        db.session.add(sent_email)
        db.session.commit()
        
        # Send the email
        msg = Message(
            subject=subject,
            recipients=[recipient_email],
            html=body if template.is_html else None,
            body=body if not template.is_html else None
        )
        
        mail.send(msg)
        
        return True
    except Exception as e:
        logger.error(f"Error sending test email: {str(e)}")
        db.session.rollback()
        return False

def queue_campaign_emails(campaign, template):
    """Queue emails for a campaign to be sent"""
    leads = campaign.leads.filter_by(status=LeadStatus.NEW).all()
    
    for lead in leads:
        # Create email record in database
        sent_email = SentEmail(
            subject=template.subject,
            body=template.body,
            recipient_email=lead.email,
            status=SentEmailStatus.QUEUED,
            template_id=template.id,
            lead_id=lead.id,
            campaign_id=campaign.id
        )
        db.session.add(sent_email)
    
    db.session.commit()
    
    # Queue emails for background sending
    queued_emails = SentEmail.query.filter_by(
        campaign_id=campaign.id,
        status=SentEmailStatus.QUEUED
    ).all()
    
    for email in queued_emails:
        lead = email.lead
        email_data = {
            'email_id': email.id,
            'template': template,
            'lead': lead,
            'recipient_email': lead.email
        }
        email_queue.put(email_data)
    
    return len(queued_emails)

def send_email_now(email_id, template, lead, recipient_email):
    """Send an email immediately"""
    try:
        # Personalize content
        subject, body = personalize_email_content(template, lead)
        
        # Update email record
        sent_email = SentEmail.query.get(email_id)
        sent_email.subject = subject
        sent_email.body = body
        sent_email.status = SentEmailStatus.SENT
        sent_email.sent_at = datetime.utcnow()
        
        # Create interaction record
        interaction = LeadInteraction(
            interaction_type=LeadInteractionType.EMAIL_SENT,
            lead_id=lead.id,
            email_id=email_id,
            details=f"Email sent at {datetime.utcnow()}"
        )
        db.session.add(interaction)
        
        # Update lead status
        lead.status = LeadStatus.CONTACTED
        lead.updated_at = datetime.utcnow()
        
        # Send the email
        msg = Message(
            subject=subject,
            recipients=[recipient_email],
            html=body if template.is_html else None,
            body=body if not template.is_html else None
        )
        
        mail.send(msg)
        
        # Update status to delivered
        sent_email.status = SentEmailStatus.DELIVERED
        db.session.commit()
        
        # Respect rate limiting
        time.sleep(60 / current_app.config['MAX_EMAILS_PER_HOUR'])
        
    except smtplib.SMTPException as e:
        logger.error(f"SMTP error sending email: {str(e)}")
        sent_email.status = SentEmailStatus.FAILED
        db.session.commit()
        
    except Exception as e:
        logger.error(f"Error sending email: {str(e)}")
        sent_email.status = SentEmailStatus.FAILED
        db.session.commit()
        raise

def stop_email_processor():
    """Stop the email processing thread"""
    email_queue.put(None)  # Sentinel value
    email_thread.join()