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
  
  def test_codes_store_creates_a_new_code_in_db(self):
    code = CodeFactory.build()

    response = self.client().post("/codes/", data={
      'code': code.code,
      'title': code.title
    })
    self.assertEqual(response.status_code, 201)

    response_json = response.json
    
    schema = self.json_schema_from_file("code.json")
    validate(response_json, schema=schema)
  
  def test_codes_store_can_create_a_new_code_in_with_a_parent_id(self):
    parent_code = CodeFactory.create()
    parent_code.save()
    parent_code_id = parent_code.id
    code = CodeFactory.build()
    response = self.client().post("/codes/", data={
      'code': code.code,
      'title': code.title,
      'parentCodeId': parent_code_id
    })
    self.assertEqual(response.status_code, 201)

    response_json = response.json
    
    schema = self.json_schema_from_file("code.json")
    validate(response_json, schema=schema)
    self.assertEqual(response_json["data"]['parentCodeId'], parent_code_id)
  
  def test_codes_store_returns_a_400_error_for_missing_code_in_request(self):
    code = CodeFactory.build()

    response = self.client().post("/codes/", data={
      'title': code.title
    })
    self.assertEqual(response.status_code, 400)
  
  def test_codes_store_returns_a_400_error_for_missing_title_in_request(self):
    code = CodeFactory.build()

    response = self.client().post("/codes/", data={
      'code': code.code
    })
    self.assertEqual(response.status_code, 400)

  def test_codes_update_returns_a_404_error_for_a_codeid_that_does_not_exist(self):
    response = self.client().patch(
      f'/codes/456788',
      data={}
    )
    self.assertEqual(response.status_code, 404)

  def test_codes_update_can_update_an_existing_code_record(self):
    code = CodeFactory.create()
    code_code = code.code
    code_title = code.title
    code.save()

    updates = CodeFactory.build()
    
    response = self.client().patch(
      f'/codes/{code.id}', 
      data={
        'code': updates.code,
        'title': updates.title
      }
    )
    self.assertEqual(response.status_code, 200)
    response_json = response.json

    schema = self.json_schema_from_file("code.json")
    validate(response_json, schema=schema)

    updated_code = Code.query.get(code.id)
    self.assertNotEqual(updated_code.code, code_code)
    self.assertNotEqual(updated_code.title, code_title)
    self.assertEqual(updated_code.code, updates.code)
    self.assertEqual(updated_code.title, updates.title)

  def test_codes_destroy_can_remove_a_record_from_the_database(self):
    code = CodeFactory.create()
    code.save()
    
    response = self.client().delete(f'/codes/{code.id}')
    self.assertEqual(response.status_code, 200)

    self.assertIsNone(Code.query.get(code.id))

    response = self.client().delete(f'/codes/{code.id}')
    self.assertEqual(response.status_code, 404)
