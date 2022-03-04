from http import HTTPStatus
from werkzeug.exceptions import BadRequest


class BadRequisiton(BadRequest):
    code = HTTPStatus.BAD_REQUEST
    description = {"error_message": "key value already registered"}