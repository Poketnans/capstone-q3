from http import HTTPStatus
from app.services.payload_eval import payload_eval
from flask import current_app, jsonify, request
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from app.models import Storage
from app.errors import InvalidValueTypesError


@jwt_required()
def update(id):

    session: Session = current_app.db.session

    try:
        data = request.get_json()

        item: Storage = Storage.query.get(id)
        if not item:
            raise NoResultFound

        if(data):
            optional_fields = ["name", "quantity", "description", "validity"]
            field_types = {
                'name': str,
                'quantity': int,
                'description': str,
                'validity': str
            }
            data = payload_eval(data, optional_fields, **field_types)
            for key, value in data.items():
                setattr(item, key, value)

        session.add(item)
        session.commit()

        return jsonify(item), HTTPStatus.OK
    except InvalidValueTypesError as err:
        return jsonify(err.description), HTTPStatus.BAD_REQUEST
    except NoResultFound as e:
        return {"msg": "user not found"}, HTTPStatus.NOT_FOUND
