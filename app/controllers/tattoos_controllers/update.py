from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from app.classes.app_with_db import current_app
from app.decorators import verify_payload
from app.models import Tattooist, Tattoo
from app.errors import NotAnAdmin


@jwt_required()
@verify_payload(
    fields_and_types={
        "size": str,
        'colors': bool,
        "body_parts": str,
        "id_tattoist": str
    },
    optional=["size", "colors", "body_parts", "id_tattoist"]
)
def update(id_tattoo, payload):
    try:
        session: Session = current_app.db.session
        tattoist_jwt = get_jwt_identity()
        id_tattoist = tattoist_jwt['id']

        admin: Tattooist = Tattooist.query.get(id_tattoist)

        tattoo: Tattoo = Tattoo.query.get(id_tattoo)

        if not admin.admin:
            raise NotAnAdmin

        if not tattoo:
            raise NoResultFound

        for key, value in payload.items():
            setattr(tattoo, key, value)

        session.add(tattoo)
        session.commit()

        return jsonify(tattoo), HTTPStatus.OK
    except NotAnAdmin:
        return {"msg": "user does not have the access rights to do this"}, HTTPStatus.FORBIDDEN

    except NoResultFound:
        return {"msg": "not found"}, HTTPStatus.NOT_FOUND
