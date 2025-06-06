from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager
import uuid
import enum

class UserRole(enum.Enum):
    ADMIN = 'admin'
    USER = 'user'

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(36), unique=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.Enum(UserRole), default=UserRole.USER)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    campaigns = db.relationship('Campaign', backref='creator', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

class LeadStatus(enum.Enum):
    NEW = 'new'
    CONTACTED = 'contacted'
    INTERESTED = 'interested'
    CLOSED = 'closed'
    UNRESPONSIVE = 'unresponsive'

class LeadSource(enum.Enum):
    WEB_SCRAPE = 'web_scrape'
    MANUAL_ENTRY = 'manual_entry'
    IMPORT = 'import'

class Lead(db.Model):
    __tablename__ = 'leads'
    
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(36), unique=True, default=lambda: str(uuid.uuid4()))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True)
    phone = db.Column(db.String(20))
    company = db.Column(db.String(120))
    position = db.Column(db.String(120))
    industry = db.Column(db.String(120))
    website = db.Column(db.String(256))
    location = db.Column(db.String(120))
    status = db.Column(db.Enum(LeadStatus), default=LeadStatus.NEW)
    source = db.Column(db.Enum(LeadSource), default=LeadSource.WEB_SCRAPE)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'))
    interactions = db.relationship('LeadInteraction', backref='lead', lazy='dynamic')
    
    def __repr__(self):
        return f'<Lead {self.first_name} {self.last_name} ({self.company})>'

class CampaignStatus(enum.Enum):
    DRAFT = 'draft'
    ACTIVE = 'active'
    PAUSED = 'paused'
    COMPLETED = 'completed'

class Campaign(db.Model):
    __tablename__ = 'campaigns'
    
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(36), unique=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(120))
    description = db.Column(db.Text)
    status = db.Column(db.Enum(CampaignStatus), default=CampaignStatus.DRAFT)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    leads = db.relationship('Lead', backref='campaign', lazy='dynamic')
    emails = db.relationship('EmailTemplate', backref='campaign', lazy='dynamic')
    analytics = db.relationship('CampaignAnalytics', backref='campaign', uselist=False)
    
    def __repr__(self):
        return f'<Campaign {self.name}>'

class EmailTemplate(db.Model):
    __tablename__ = 'email_templates'
    
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(36), unique=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(120))
    subject = db.Column(db.String(256))
    body = db.Column(db.Text)
    is_html = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'))
    
    def __repr__(self):
        return f'<EmailTemplate {self.name}>'

class LeadInteractionType(enum.Enum):
    EMAIL_SENT = 'email_sent'
    EMAIL_OPENED = 'email_opened'
    LINK_CLICKED = 'link_clicked'
    REPLY_RECEIVED = 'reply_received'
    NOTE_ADDED = 'note_added'
    STATUS_CHANGED = 'status_changed'

class LeadInteraction(db.Model):
    __tablename__ = 'lead_interactions'
    
    id = db.Column(db.Integer, primary_key=True)
    interaction_type = db.Column(db.Enum(LeadInteractionType))
    details = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    lead_id = db.Column(db.Integer, db.ForeignKey('leads.id'))
    email_id = db.Column(db.Integer, db.ForeignKey('sent_emails.id'), nullable=True)
    
    def __repr__(self):
        return f'<LeadInteraction {self.interaction_type}>'

class SentEmailStatus(enum.Enum):
    QUEUED = 'queued'
    SENT = 'sent'
    DELIVERED = 'delivered'
    BOUNCED = 'bounced'
    FAILED = 'failed'

class SentEmail(db.Model):
    __tablename__ = 'sent_emails'
    
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(36), unique=True, default=lambda: str(uuid.uuid4()))
    subject = db.Column(db.String(256))
    body = db.Column(db.Text)
    recipient_email = db.Column(db.String(120))
    status = db.Column(db.Enum(SentEmailStatus), default=SentEmailStatus.QUEUED)
    sent_at = db.Column(db.DateTime)
    opened_at = db.Column(db.DateTime)
    open_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    template_id = db.Column(db.Integer, db.ForeignKey('email_templates.id'))
    lead_id = db.Column(db.Integer, db.ForeignKey('leads.id'))
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'))
    
    interactions = db.relationship('LeadInteraction', backref='email', lazy='dynamic')
    
    def __repr__(self):
        return f'<SentEmail to {self.recipient_email}>'

class CampaignAnalytics(db.Model):
    __tablename__ = 'campaign_analytics'
    
    id = db.Column(db.Integer, primary_key=True)
    emails_sent = db.Column(db.Integer, default=0)
    emails_delivered = db.Column(db.Integer, default=0)
    emails_opened = db.Column(db.Integer, default=0)
    unique_opens = db.Column(db.Integer, default=0)
    click_count = db.Column(db.Integer, default=0)
    unique_clicks = db.Column(db.Integer, default=0)
    replies_received = db.Column(db.Integer, default=0)
    bounce_rate = db.Column(db.Float, default=0.0)
    open_rate = db.Column(db.Float, default=0.0)
    click_rate = db.Column(db.Float, default=0.0)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'))
    
    def update_metrics(self):
        # Calculate metrics based on sent emails
        sent_emails = SentEmail.query.filter_by(campaign_id=self.campaign_id).all()
        
        self.emails_sent = len(sent_emails)
        self.emails_delivered = len([e for e in sent_emails if e.status in [SentEmailStatus.DELIVERED, SentEmailStatus.SENT]])
        self.emails_opened = sum(e.open_count for e in sent_emails)
        self.unique_opens = len([e for e in sent_emails if e.open_count > 0])
        self.click_count = sum(len(e.interactions.filter_by(interaction_type=LeadInteractionType.LINK_CLICKED).all()) for e in sent_emails)
        self.unique_clicks = len(set(i.lead_id for e in sent_emails for i in e.interactions.filter_by(interaction_type=LeadInteractionType.LINK_CLICKED)))
        self.replies_received = len([e for e in sent_emails if e.interactions.filter_by(interaction_type=LeadInteractionType.REPLY_RECEIVED).first()])
        
        if self.emails_sent > 0:
            self.bounce_rate = (len([e for e in sent_emails if e.status == SentEmailStatus.BOUNCED]) / self.emails_sent) * 100
            self.open_rate = (self.unique_opens / self.emails_sent) * 100
            self.click_rate = (self.unique_clicks / self.emails_sent) * 100
        
        db.session.commit()
    
    def __repr__(self):
        return f'<CampaignAnalytics for campaign {self.campaign_id}>'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))