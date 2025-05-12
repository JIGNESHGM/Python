from flask_pymongo import PyMongo
from flask import current_app
from datetime import datetime
import uuid

mongo = PyMongo()

def get_db():
    return mongo.db

def init_db(app):
    mongo.init_app(app)
    # Create indexes
    db = get_db()
    db.leads.create_index('email', unique=True)
    db.leads.create_index('company_name')
    db.campaigns.create_index('lead_id')
    db.campaigns.create_index('tracking_token', unique=True)

def insert_lead(lead_data):
    db = get_db()
    lead_data['date_added'] = datetime.utcnow()
    lead_data['last_updated'] = datetime.utcnow()
    result = db.leads.insert_one(lead_data)
    return result.inserted_id

def get_lead(lead_id):
    db = get_db()
    return db.leads.find_one({'_id': lead_id})

def get_all_leads():
    db = get_db()
    return list(db.leads.find())

def update_lead(lead_id, update_data):
    db = get_db()
    update_data['last_updated'] = datetime.utcnow()
    return db.leads.update_one(
        {'_id': lead_id},
        {'$set': update_data}
    )

def insert_campaign(campaign_data):
    db = get_db()
    campaign_data['tracking_token'] = str(uuid.uuid4())
    campaign_data['created_at'] = datetime.utcnow()
    campaign_data['updated_at'] = datetime.utcnow()
    result = db.campaigns.insert_one(campaign_data)
    return result.inserted_id, campaign_data['tracking_token']

def update_campaign(campaign_id, update_data):
    db = get_db()
    update_data['updated_at'] = datetime.utcnow()
    return db.campaigns.update_one(
        {'_id': campaign_id},
        {'$set': update_data}
    )

def get_campaigns_for_lead(lead_id):
    db = get_db()
    return list(db.campaigns.find({'lead_id': lead_id}))

def get_campaign_by_token(tracking_token):
    db = get_db()
    return db.campaigns.find_one({'tracking_token': tracking_token})

def get_all_campaigns():
    db = get_db()
    return list(db.campaigns.find())

def get_analytics_data():
    db = get_db()
    
    total_leads = db.leads.count_documents({})
    total_campaigns = db.campaigns.count_documents({})
    
    pipeline = [
        {
            '$group': {
                '_id': None,
                'sent': {'$sum': {'$cond': [{'$eq': ['$email_sent', True]}, 1, 0]}},
                'opened': {'$sum': {'$cond': [{'$eq': ['$email_opened', True]}, 1, 0]}},
                'clicked': {'$sum': {'$cond': [{'$eq': ['$link_clicked', True]}, 1, 0]}},
                'responded': {'$sum': {'$cond': [{'$eq': ['$response_received', True]}, 1, 0]}},
                'hot': {'$sum': {'$cond': [{'$eq': ['$lead_category', 'hot']}, 1, 0]}},
                'warm': {'$sum': {'$cond': [{'$eq': ['$lead_category', 'warm']}, 1, 0]}},
                'cold': {'$sum': {'$cond': [{'$eq': ['$lead_category', 'cold']}, 1, 0]}}
            }
        }
    ]
    
    stats = list(db.campaigns.aggregate(pipeline))
    if stats:
        stats = stats[0]
        stats.pop('_id', None)
    else:
        stats = {
            'sent': 0,
            'opened': 0,
            'clicked': 0,
            'responded': 0,
            'hot': 0,
            'warm': 0,
            'cold': 0
        }
    
    stats['total_leads'] = total_leads
    stats['total_campaigns'] = total_campaigns
    
    return stats