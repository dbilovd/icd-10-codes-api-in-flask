from flask import Blueprint, jsonify, request
from app.models.code import Code

codes_controller = Blueprint('codes', __name__)


@codes_controller.route("/")
def fetch_all_codes():
  page_to_fetch = request.data.get("page")
  
  paginator = Code.query.paginate(
    per_page=20,
    page=page_to_fetch
  )
  
  formatted_codes = []
  if paginator.items is not None:
    for code in paginator.items:
      formatted_codes.append(
        code.__repr__()
      )
  
  response_data = {
    'responseCode': 200,
    'responseMessage': 'Success',
    'data': formatted_codes,
    'meta': {
      'totalPages': paginator.pages,
      'totalItems': paginator.total,
      'itemsPerPage': paginator.per_page,
      'currentPage': paginator.page,
      'previousPage': paginator.prev_num,
      'nextPage': paginator.next_num,
    }
  }

  response = jsonify(response_data)
  response.status_code = 200

  return response
