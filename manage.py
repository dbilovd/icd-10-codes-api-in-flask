import os
import unittest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.models import db

app = create_app(
  config_name=os.getenv('FLASK_ENV')
)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
  tests = unittest.TestLoader().discover(
      './tests',
      pattern='test_*.py'
    )
  test_results = unittest.TextTestRunner(verbosity=2).run(tests)
  return 0 if test_results.wasSuccessful() else 1

if __name__ == '__main__':
  manager.run()
