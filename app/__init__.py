from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt




bootstrap = Bootstrap()
db = SQLAlchemy()
bcrypt = Bcrypt()





def create_app(config_name):
    app = Flask(__name__)


    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # bcrypt = Bcrypt(app)




    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)




    # Will add the views and forms
    #registering a blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # from app.auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint,url_prefix='/authenticate')




    # #SETTING UP CONFIGURATION
    # # from .request import configure_request
    # configure_request(app)
    
   
    return app
        