import os
import unittest
from flask_script import Manager
from app import create_app

app = create_app(
  config_name=os.getenv('FLASK_ENV')
)
manager = Manager(app)

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
