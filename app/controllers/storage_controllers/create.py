from http import HTTPStatus
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import DataError
from app.classes.app_with_db import current_app
from app.models import Storage
from app.decorators import verify_payload, validator


@validator(date="validity")
@verify_payload(
    fields_and_types={
        "name": str,
        "quantity": int,
        "description": str,
        "validity": str
    },
    optional=['description']
)
@jwt_required()
def create():

    payload = request.get_json()

    session = current_app.db.session

    try:

        new_item = Storage(**payload)

        session.add(new_item)
        session.commit()

    except DataError as err:
        resp = {
            'msg': 'Invalid date format. Try DD/MM/YYY'
        }
        return jsonify(resp), HTTPStatus.CONFLICT

    return jsonify(new_item), HTTPStatus.CREATED
