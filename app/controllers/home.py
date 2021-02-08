from flask import Blueprint, jsonify

home_controller = Blueprint('home', __name__)

@home_controller.route("/")
def home():
  response_data = {
    'responseCode': 200,
    'responseMessage': 'Welcome to our ICD-10 API'
  }

  response = jsonify(response_data)
  response.status_code = 200

  return response

  
