from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from app.classes.app_with_db import current_app
from app.decorators import verify_payload
from app.errors import FieldMissingError, InvalidValueTypesError
from app.models import Tattooist, Tattoo, Material
from app.errors import NotAnAdmin
from app.services import payload_eval


@jwt_required()
@verify_payload(
    fields_and_types={
        "size": str,
        'colors': bool,
        "body_parts": str,
        "id_tattoist": str,
        "materials": list
    },
    optional=["size", "colors", "body_parts", "id_tattoist", "materials"]
)
def update(id_tattoo, payload: dict):
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

        materials = payload.pop("materials", None)
        if materials:
            materials_fields = {"id_product": str,
                                "id_tattoo": str, "quantity": int}
            for material_info in materials:
                material_payload = payload_eval(
                    material_info,
                    **materials_fields
                )
                new_material = Material(**material_payload)
                tattoo.materials.append(new_material)

        for key, value in payload.items():
            setattr(tattoo, key, value)

        session.add(tattoo)
        session.commit()

        return jsonify(tattoo), HTTPStatus.OK

    except InvalidValueTypesError as err:
        return jsonify(err.description), err.code
    except FieldMissingError as err:
        return jsonify(err.description), err.code
    except NotAnAdmin:
        return {"msg": "user does not have the access rights to do this"}, HTTPStatus.FORBIDDEN

    except NoResultFound:
        return {"msg": "not found"}, HTTPStatus.NOT_FOUND
