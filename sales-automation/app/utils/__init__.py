# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from config import Config
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'

    # Register blueprints
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register error handlers
    from app.errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)

    return app

from app import models