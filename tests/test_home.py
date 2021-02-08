import unittest
import os
from app import create_app

class HomeTest(unittest.TestCase):

  def setUp(self):
    self.app = create_app(
      os.getenv("FLASK_ENV")
    )
    self.client = self.app.test_client
  

  def test_api_home_page_returns_a_200_status(self):
    response = self.client().get("/")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json, {
      'responseCode': 200,
      'responseMessage': 'Welcome to our ICD-10 API'
    })


if __name__ == '__main__':
  unittest.main()
