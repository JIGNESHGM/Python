from datetime import datetime
from app.utils.mongo_handler import get_db

class Lead:
    @staticmethod
    def create(company_name, email=None, contact_person=None, industry=None, 
               website=None, location=None, source='web'):
        lead_data = {
            'company_name': company_name,
            'email': email,
            'contact_person': contact_person,
            'industry': industry,
            'website': website,
            'location': location,
            'source': source
        }
        return get_db().leads.insert_one(lead_data)
    
    @staticmethod
    def get_all():
        return list(get_db().leads.find())
    
    @staticmethod
    def get_by_id(lead_id):
        return get_db().leads.find_one({'_id': lead_id})
    
    @staticmethod
    def update(lead_id, update_data):
        update_data['last_updated'] = datetime.utcnow()
        return get_db().leads.update_one(
            {'_id': lead_id},
            {'$set': update_data}
        )

class Campaign:
    @staticmethod
    def create(lead_id, email_sent=False, email_opened=False, 
               link_clicked=False, response_received=False, 
               lead_score=0.5, lead_category='cold'):
        campaign_data = {
            'lead_id': lead_id,
            'email_sent': email_sent,
            'email_opened': email_opened,
            'link_clicked': link_clicked,
            'response_received': response_received,
            'lead_score': lead_score,
            'lead_category': lead_category,
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow()
        }
        return get_db().campaigns.insert_one(campaign_data)
    
    @staticmethod
    def get_by_lead(lead_id):
        return list(get_db().campaigns.find({'lead_id': lead_id}))
    
    @staticmethod
    def update(campaign_id, update_data):
        update_data['updated_at'] = datetime.utcnow()
        return get_db().campaigns.update_one(
            {'_id': campaign_id},
            {'$set': update_data}
        )
    
    @staticmethod
    def get_by_token(tracking_token):
        return get_db().campaigns.find_one({'tracking_token': tracking_token})