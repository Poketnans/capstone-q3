from http import HTTPStatus
from flask import current_app, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from app.models import Tattooist, Tattoo
from app.services.payload_eval import payload_eval
from app.errors import InvalidValueTypesError, NotAnAdmin


@jwt_required()
def update(id_tattoo):
    try:
        session: Session = current_app.db.session
        tattoist_jwt = get_jwt_identity()
        id_tattoist = tattoist_jwt['id']
        data = request.get_json()

        admin: Tattooist = Tattooist.query.get(id_tattoist)

        tattoo: Tattoo = Tattoo.query.get(id_tattoo)

        if not admin.admin:
            raise NotAnAdmin

        if not tattoo:
            raise NoResultFound

        if(data):
            optional_fields = ["size", "colors", "body_parts", "id_tattoist"]
            field_types = {
                "size": str,
                'colors': bool,
                "body_parts": str,
                "id_tattoist": str
            }
            data = payload_eval(data, optional_fields, **field_types)
            for key, value in data.items():
                setattr(tattoo, key, value)

        session.add(tattoo)
        session.commit()

        return jsonify(tattoo), HTTPStatus.OK

    except InvalidValueTypesError as err:
        return jsonify(err.description), err.code

    except NotAnAdmin as e:
        return {"msg": "user does not have the access rights to do this"}, HTTPStatus.FORBIDDEN

    except NoResultFound as e:
        return {"msg": "tattoo not found"}, HTTPStatus.NOT_FOUND
