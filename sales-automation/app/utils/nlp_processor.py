import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os
from app.models import Lead, Campaign
from datetime import datetime

class LeadScorer:
    def __init__(self):
        self.model_path = 'app/data/lead_scorer_model.pkl'
        self.vectorizer_path = 'app/data/tfidf_vectorizer.pkl'
        self.model = None
        self.vectorizer = None
        self.load_models()
        
    def load_models(self):
        """Load pre-trained models if they exist"""
        if os.path.exists(self.model_path) and os.path.exists(self.vectorizer_path):
            self.model = joblib.load(self.model_path)
            self.vectorizer = joblib.load(self.vectorizer_path)
        
    def prepare_training_data(self):
        """Prepare data for model training"""
        campaigns = Campaign.get_all()
        leads = Lead.get_all()
        
        lead_map = {str(lead['_id']): lead for lead in leads}
        
        data = []
        for campaign in campaigns:
            if 'response_received' not in campaign:
                continue
                
            lead = lead_map.get(str(campaign['lead_id']))
            if not lead:
                continue
                
            data.append({
                'company_name': lead.get('company_name', ''),
                'industry': lead.get('industry', ''),
                'location': lead.get('location', ''),
                'response': int(campaign.get('response_received', False)),
                'opened': int(campaign.get('email_opened', False)),
                'clicked': int(campaign.get('link_clicked', False))
            })
            
        if not data:
            return None
            
        return pd.DataFrame(data)
            
    def train_model(self):
        """Train the lead scoring model"""
        df = self.prepare_training_data()
        if df is None or len(df) < 50:
            print("Not enough data to train model")
            return False
            
        # Feature engineering
        df['features'] = df['company_name'] + ' ' + df['industry'] + ' ' + df['location']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            df['features'], 
            df['response'], 
            test_size=0.2, 
            random_state=42
        )
        
        # Vectorize text
        self.vectorizer = TfidfVectorizer(max_features=1000)
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)
        
        # Train model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train_vec, y_train)
        
        # Save models
        joblib.dump(self.model, self.model_path)
        joblib.dump(self.vectorizer, self.vectorizer_path)
        
        return True
        
    def predict_lead_score(self, lead):
        """Predict lead score for a new lead"""
        if not self.model or not self.vectorizer:
            return 0.5  # Default score if model not trained
            
        features = f"{lead.get('company_name', '')} {lead.get('industry', '')} {lead.get('location', '')}"
        features_vec = self.vectorizer.transform([features])
        score = self.model.predict_proba(features_vec)[0][1]
        
        return score
        
    def categorize_leads(self):
        """Categorize leads into hot/warm/cold based on their scores"""
        leads = Lead.get_all()
        for lead in leads:
            score = self.predict_lead_score(lead)
            category = 'hot' if score > 0.7 else 'warm' if score > 0.4 else 'cold'
            
            # Update all campaigns for this lead
            campaigns = Campaign.get_by_lead(lead['_id'])
            for campaign in campaigns:
                Campaign.update(campaign['_id'], {
                    'lead_score': score,
                    'lead_category': category
                })