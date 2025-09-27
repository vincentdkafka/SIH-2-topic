"""
Flask Application Factory
Creates and configures the Flask application instance.
"""

from flask import Flask
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def create_app():
    """
    Create and configure the Flask application.
    
    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
    
    # Configure the app
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
    app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    # Register blueprints/routes
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
