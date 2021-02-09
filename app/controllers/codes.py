from flask import Blueprint, request
from app.models.code import Code
from . import respond

codes_controller = Blueprint('codes', __name__)

@codes_controller.route("/", methods=["GET"])
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
  
  meta = {
    'totalPages': paginator.pages,
    'totalItems': paginator.total,
    'itemsPerPage': paginator.per_page,
    'currentPage': paginator.page,
    'previousPage': paginator.prev_num,
    'nextPage': paginator.next_num,
  }

  return respond(
    data=formatted_codes,
    meta=meta
  )

@codes_controller.route("/", methods=["POST"])
def store_a_new_code():
  request_code = request.data.get("code")
  request_title = request.data.get("title")

  if request_code is None or request_title is None:
    return respond(
      status_code=400,
      message='Invalid Data Provided'
    )

  code = Code(code=request_code, title=request_title)
  code.save()

  return respond(
    data=code.__repr__(),
    status_code=201
  )
