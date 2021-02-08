import os

# Config Class
class Config(object):
  DEBUG = False
  TESTING = False
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

# Development Config Class
class DevelopmentConfig(Config):
  DEBUG = True


# Testing Config Class
class TestingConfig(Config):
  DEBUG = True
  TESTING = True


# Testing Config Class
class ProductionConfig(Config):
  DEBUG = False
  TESTING = False


app_config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig,
  'production': ProductionConfig
}
