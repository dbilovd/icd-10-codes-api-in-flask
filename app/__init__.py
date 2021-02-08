from flask_api import FlaskAPI
from instance.config import app_config
from app.controllers.home import home_controller
from app.controllers.codes import codes_controller

def create_app(config_name):
  # Set default config to use
  config_name = "development" if config_name == None else config_name

  # Create application
  app = FlaskAPI(__name__, instance_relative_config=True)
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile('config.py')

  # Setup DB
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

  from app.models import db
  db.init_app(app)
  
  # Register blueprints
  app.register_blueprint(
    home_controller,
    url_prefix='/'
  )
  app.register_blueprint(
    codes_controller,
    url_prefix='/codes'
  )

  # Return app instance
  return app

