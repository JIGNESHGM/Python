from flask import Flask
from flask_mail import Mail
from config import Config
from app.utils.mongo_handler import init_db, mongo

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    mail.init_app(app)
    init_db(app)
    
    # Register blueprints
    from app.routes import bp
    app.register_blueprint(bp)
    
    return app