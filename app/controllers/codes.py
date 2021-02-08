from flask import Blueprint, jsonify
from app.models.code import Code

codes_controller = Blueprint('codes', __name__)


@codes_controller.route("/")
def fetch_all_codes():
  codes = Code.query.all()
  
  formatted_codes = []
  for code in codes:
    formatted_codes.append(
      code.__repr__()
    )
  
  response_data = {
    'responseCode': 200,
    'responseMessage': 'Success',
    'data': formatted_codes
  }

  response = jsonify(response_data)
  response.status_code = 200

  return response
