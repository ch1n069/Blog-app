from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
bootstrap = Bootstrap()
db = SQLAlchemy()
def create_app(config_name):
    app = Flask(_name_)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # Will add the views and forms
    #registering a blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')
    #SETTING UP CONFIGURATION
    from .request import configure_request
    configure_request(app)
    
   
    return app
        