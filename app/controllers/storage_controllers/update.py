from http import HTTPStatus
from app.decorators import verify_payload
from flask import current_app, jsonify, request
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from app.models import Storage


@verify_payload(
    fields_and_types={
        'name': str,
        'quantity': int,
        'description': str,
        'validity': str
    },
    optional=["name", "quantity", "description", "validity"]
)
@jwt_required()
def update(id):

    session: Session = current_app.db.session

    try:
        payload = request.get_json()

        item: Storage = Storage.query.get(id)
        if not item:
            raise NoResultFound

        for key, value in payload.items():
            setattr(item, key, value)

        session.add(item)
        session.commit()

        return jsonify(item), HTTPStatus.OK

    except NoResultFound as e:
        return {"msg": "user not found"}, HTTPStatus.NOT_FOUND
