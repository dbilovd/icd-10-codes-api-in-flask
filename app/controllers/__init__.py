from flask import jsonify

def respond(data=None, status_code=200, message='Success', meta=None):
  results = {
      'responseCode': status_code,
      'responseMessage': message,
  }

  if data:
    results['data'] = data

  if meta:
    results['meta'] = meta

  response = jsonify(results)
  response.status_code = status_code
  return response
