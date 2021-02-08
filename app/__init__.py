from flask_api import FlaskAPI
from instance.config import app_config
from app.controllers.home import home_controller

def create_app(config_name):
  # Set default config to use
  config_name = "development" if config_name == None else config_name

  # Create application
  app = FlaskAPI(__name__, instance_relative_config=True)
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile('config.py')
  
  # Register blueprints
  app.register_blueprint(
    home_controller,
    url_prefix='/'
  )

  # Return app instance
  return app

