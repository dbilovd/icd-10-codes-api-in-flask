import unittest
import os
import json
from app import create_app
from app.models import db
from app.models.code import Code
from app.models.factories.code import CodeFactory
from jsonschema import validate

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

  def json_schema_from_file(self, filename):
    path = os.path.join(
      os.path.dirname(__file__),
      os.path.join('support', filename)
    )
    with open(path) as schema_file:
      return json.loads(schema_file.read())

  def test_codes_index_returns_a_200_status_code(self):
    response = self.client().get("/codes/")
    self.assertEqual(response.status_code, 200)

  def test_codes_index_returns_any_codes_available(self):
    code = CodeFactory.create()

    response = self.client().get("/codes/")
    response_json = response.json
    schema = self.json_schema_from_file("codes.json")
    validate(response_json, schema=schema)
    
    expected_code = response_json['data'][0]
    self.assertEqual(expected_code['codeId'], code.id)
  
  def test_codes_index_returns_a_paginated_set_of_20_codes(self):
    CodeFactory.create_batch(21)

    response = self.client().get("/codes/")
    response_json = response.json
    self.assertEqual(len(response_json['data']), 20)

    self.assertEqual(response_json['meta']['currentPage'], 1)
    self.assertEqual(response_json['meta']['previousPage'], None)
    self.assertEqual(response_json['meta']['nextPage'], 2)
    self.assertEqual(response_json['meta']['totalPages'], 2)
    self.assertEqual(response_json['meta']['itemsPerPage'], 20)
    self.assertEqual(response_json['meta']['totalItems'], 21)
  
  def test_codes_index_allows_for_fetching_a_particular_paginated_page(self):
    CodeFactory.create_batch(21)

    response = self.client().get("/codes/?page=2")
    response_json = response.json
    self.assertEqual(len(response_json['data']), 1)

    self.assertEqual(response_json['meta']['currentPage'], 2)
    self.assertEqual(response_json['meta']['previousPage'], 1)
    self.assertEqual(response_json['meta']['nextPage'], None)
    self.assertEqual(response_json['meta']['totalPages'], 2)
    self.assertEqual(response_json['meta']['itemsPerPage'], 20)
    self.assertEqual(response_json['meta']['totalItems'], 21)
  
  def test_codes_index_returns_a_404_error_code_for_a_page_that_does_not_exists(self):
    CodeFactory.create_batch(2)

    response = self.client().get("/codes/?page=2")
    self.assertEqual(response.status_code, 404)
