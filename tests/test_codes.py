import unittest
from app import create_app
from app.models import db
from app.models.code import Code

class CodesTest(unittest.TestCase):

  def setUp(self):
    self.app = create_app("testing")
    self.client = self.app.test_client
    
    with self.app.app_context():
      db.session.close()
      db.drop_all()
      db.create_all()

  def tearDown(self):
    with self.app.app_context():
      db.session.close()
      db.drop_all()

  def test_codes_index_returns_a_200_status_code(self):
    response = self.client().get("/codes/")
    self.assertEqual(response.status_code, 200)

  def test_codes_index_returns_any_codes_available(self):
    code = Code(code = "123", title="New Code")
    code.save()

    response = self.client().get("/codes/")
    response_json = response.json
    self.assertTrue('data' in response_json)
    self.assertEqual(len(response_json['data']), 1)
    
    expected_code = response_json['data'][0]
    self.assertEqual(expected_code['codeId'], code.id)
    self.assertEqual(expected_code['title'], code.title)
    self.assertEqual(expected_code['code'], code.code)
