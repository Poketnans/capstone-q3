from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import DataError
import werkzeug
from app.classes.app_with_db import current_app
from app.models import Storage, Tattooist
from app.decorators import verify_payload, validator

from app.errors import NotAnAdmin


@validator(date="validity")
@verify_payload(
    fields_and_types={
        "name": str,
        "quantity": int,
        "description": str,
        "validity": str
    },
    optional=['description'],
    not_empty_string=['name', 'validity']
)
@jwt_required()
def create(payload):

    session = current_app.db.session

    try:
        id_tattooist = get_jwt_identity().get("id")

        tatooist: Tattooist = session.query(Tattooist).filter_by(id=id_tattooist).first_or_404(
            description={"msg": "tattooist not found"})

        if not tatooist.admin:
            raise NotAnAdmin

    except werkzeug.exceptions.NotFound as err:
        return err.description, HTTPStatus.CONFLICT
    except NotAnAdmin:
        return {"msg": "you don't have the right privileges"}, HTTPStatus.FORBIDDEN

    new_item = Storage(**payload)

    session.add(new_item)
    session.commit()

    return jsonify(new_item), HTTPStatus.CREATED
