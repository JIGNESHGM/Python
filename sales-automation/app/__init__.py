from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from config import config
import os
import spacy
import openai
from .utils.analytics import AnalyticsEngine

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
csrf = CSRFProtect()
analytics_engine = AnalyticsEngine()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)
    
    # Load AI models
    try:
        app.nlp = spacy.load(app.config['NLP_MODEL'])
    except OSError:
        # Download the model if not available
        from spacy.cli import download
        download(app.config['NLP_MODEL'])
        app.nlp = spacy.load(app.config['NLP_MODEL'])
    
    # Configure OpenAI
    openai.api_key = app.config['OPENAI_API_KEY']
    
    # Initialize analytics engine
    analytics_engine.init_app(app)
    
    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Error handlers
    register_error_handlers(app)
    
    # CLI commands
    register_commands(app)
    
    return app

def register_error_handlers(app):
    from flask import render_template
    
    @app.errorhandler(403)
    def forbidden(e):
        return render_template('error.html', error_code=403, message="Forbidden"), 403
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html', error_code=404, message="Page not found"), 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('error.html', error_code=500, message="Internal server error"), 500

def register_commands(app):
    import click
    from flask.cli import with_appcontext
    
    @app.cli.command("init-db")
    @with_appcontext
    def init_db():
        """Initialize the database."""
        db.create_all()
        click.echo("Database initialized.")
    
    @app.cli.command("scrape-sample")
    @with_appcontext
    def scrape_sample():
        """Run sample scraping job."""
        from .utils.scraping import run_sample_scrape
        run_sample_scrape()
        click.echo("Sample scraping completed.")