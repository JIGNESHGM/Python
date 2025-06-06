import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

class Config:
    # Security settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    CSRF_ENABLED = True
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///sales_automation.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Email configuration
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@salesautomation.com')
    
    # Scraping configuration
    SCRAPING_API_KEY = os.getenv('SCRAPING_API_KEY')
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    
    # Analytics configuration
    ANALYTICS_DOMAIN = os.getenv('ANALYTICS_DOMAIN', 'yourdomain.com')
    
    # Rate limiting
    MAX_EMAILS_PER_HOUR = int(os.getenv('MAX_EMAILS_PER_HOUR', 50))
    
    # File uploads
    UPLOAD_FOLDER = Path('app/static/uploads')
    ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
    
    # AI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    NLP_MODEL = "en_core_web_md"  # Medium spaCy model
    
    @staticmethod
    def init_app(app):
        # Ensure upload folder exists
        Config.UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}