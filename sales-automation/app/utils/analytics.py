from app import db
from app.models import CampaignAnalytics, SentEmail, LeadInteraction, Lead
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AnalyticsEngine:
    def __init__(self):
        self.initialized = False
    
    def init_app(self, app):
        self.app = app
        self.initialized = True
    
    def update_campaign_analytics(self, campaign_id):
        """Update analytics for a specific campaign"""
        with self.app.app_context():
            try:
                campaign = Campaign.query.get(campaign_id)
                if campaign and campaign.analytics:
                    campaign.analytics.update_metrics()
                    db.session.commit()
            except Exception as e:
                logger.error(f"Error updating campaign analytics: {str(e)}")
                db.session.rollback()
    
    def generate_daily_report(self):
        """Generate a daily analytics report"""
        with self.app.app_context():
            try:
                # Overall statistics
                total_leads = Lead.query.count()
                new_leads_today = Lead.query.filter(
                    Lead.created_at >= datetime.utcnow() - timedelta(days=1)
                ).count()
                
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
                        'replies': analytics.replies_received
                    })
                
                # Lead source distribution
                lead_sources = db.session.query(
                    Lead.source,
                    func.count(Lead.id).label('count')
                ).group_by(Lead.source).all()
                
                # Create visualizations
                charts = self._create_charts(campaign_data)
                
                return {
                    'date': datetime.utcnow().date(),
                    'total_leads': total_leads,
                    'new_leads_today': new_leads_today,
                    'campaign_data': campaign_data,
                    'lead_sources': lead_sources,
                    'charts': charts
                }
                
            except Exception as e:
                logger.error(f"Error generating daily report: {str(e)}")
                return None
    
    def _create_charts(self, campaign_data):
        """Create chart visualizations"""
        charts = {}
        
        try:
            # Campaign performance bar chart
            df = pd.DataFrame(campaign_data)
            if not df.empty:
                fig, ax = plt.subplots(figsize=(10, 6))
                df.plot.bar(x='name', y=['open_rate', 'click_rate'], ax=ax)
                ax.set_title('Campaign Performance')
                ax.set_ylabel('Rate (%)')
                ax.set_xlabel('Campaign')
                plt.tight_layout()
                
                buf = BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                charts['campaign_performance'] = base64.b64encode(buf.read()).decode('utf-8')
                plt.close()
                
            # Lead source pie chart
            lead_sources = db.session.query(
                Lead.source,
                func.count(Lead.id).label('count')
            ).group_by(Lead.source).all()
            
            if lead_sources:
                sources, counts = zip(*lead_sources)
                fig, ax = plt.subplots(figsize=(8, 8))
                ax.pie(counts, labels=sources, autopct='%1.1f%%')
                ax.set_title('Lead Sources')
                plt.tight_layout()
                
                buf = BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                charts['lead_sources'] = base64.b64encode(buf.read()).decode('utf-8')
                plt.close()
                
        except Exception as e:
            logger.error(f"Error creating charts: {str(e)}")
        
        return charts

def generate_analytics_report():
    """Generate a comprehensive analytics report"""
    engine = AnalyticsEngine()
    return engine.generate_daily_report()