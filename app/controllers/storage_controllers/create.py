from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import DataError

from app.classes.app_with_db import current_app
from app.errors import FieldMissingError, InvalidValueTypesError
from app.models import Storage
from app.services.payload_eval import payload_eval


@jwt_required()
def create():

    payload = request.get_json()

    session = current_app.db.session

    try:
        # TODO: Vatidar data
        fields = {
            "name": str,
            "quantity": int,
            "description": str,
            "validity": str
        }

        optional_fields = ['description']

        payload = payload_eval(data=payload, optional=optional_fields, **fields)

        new_item = Storage(**payload)

        session.add(new_item)
        session.commit()

    except DataError as err:
        resp = {
            'msg': 'Invalid date format. Try DD/MM/YYY'
        }
        return jsonify(resp), HTTPStatus.CONFLICT

    except FieldMissingError as err:
        return jsonify(err.description), err.code

    except InvalidValueTypesError as err:
        return jsonify(err.description), err.code

    return jsonify(new_item), HTTPStatus.CREATED
