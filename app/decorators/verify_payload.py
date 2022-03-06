from http import HTTPStatus
from json import JSONDecodeError
from flask import jsonify, request
from functools import wraps

from app.errors import FieldMissingError, InvalidValueTypesError, JSONNotFound
from app.services.get_data_with_images import get_data_with_images
from app.services import payload_eval


def verify_payload(optional: list = [], **fields_and_types):
    def received_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                data = get_data_with_images()

                filtered_data = payload_eval(data, optional, **fields_and_types)

                return func(*args, payload=filtered_data, **kwargs)

            except JSONDecodeError:
                return {"msg": "JSON in invalid format"}, HTTPStatus.BAD_REQUEST
            except InvalidValueTypesError as err:
                return {"msg": f"{err.description}"}, err.code
            except FieldMissingError as err:
                return jsonify(err.description), err.code
            except JSONNotFound as err:
                return {"msg": f"{err.describe}"}, err.status_code
        return wrapper
    return received_function
