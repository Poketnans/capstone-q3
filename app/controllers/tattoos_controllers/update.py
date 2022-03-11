from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from psycopg2.errors import InvalidTextRepresentation
import werkzeug


from app.classes.app_with_db import current_app
from app.decorators import verify_payload
from app.errors import FieldMissingError, InvalidValueTypesError, UnavaliableItemQuantityError
from app.models import Tattooist, Tattoo, Material, Storage, TattooImage
from app.errors import NotAnAdmin
from app.services import payload_eval, get_files


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
        id_tattooist = tattoist_jwt['id']

        tattoist = Tattooist.query.filter_by(id=id_tattooist).first()

        if not tattoist:
            raise NotAnAdmin

        tattoo: Tattoo = Tattoo.query.get(id_tattoo)

        if not tattoo:
            raise NoResultFound

        files = get_files()
        if files:
            for file in files:
                image_payload = {
                    "image_bin": file.file_bin,
                    "image_mimetype": file.mimetype,
                    "image_name_hash": file.filename,
                    "id_tattoo": tattoo.id
                }

                new_image = TattooImage(**image_payload)
                tattoo.image_models.append(new_image)

        materials = payload.pop("materials", None)
        if materials:
            materials_fields = {"id_item": str, "quantity": int}
            for material_info in materials:
                material_info['id_tattoo'] = id_tattoo

                item: Storage = Storage.query.get_or_404(material_info['id_item'],
                                                         description={"msg": "storage item not found"})

                material_payload = payload_eval(
                    material_info,
                    **materials_fields
                )

                if item.quantity < material_payload["quantity"]:
                    raise UnavaliableItemQuantityError(item)

                new_material = Material(**material_payload)
                tattoo.materials.append(new_material)

                item.quantity -= new_material.quantity

        for key, value in payload.items():
            setattr(tattoo, key, value)

        session.add(tattoo)
        session.commit()

        return jsonify(tattoo), HTTPStatus.OK

    except InvalidValueTypesError as err:
        return jsonify(err.description), err.code
    except FieldMissingError as err:
        return jsonify(err.description), err.code
    except UnavaliableItemQuantityError as err:
        return jsonify(err.description), err.code
    except NotAnAdmin:
        return jsonify({"msg": "you don't have the right privileges"}), HTTPStatus.FORBIDDEN

    except NoResultFound:
        return jsonify({"msg": "tattoo not found"}), HTTPStatus.NOT_FOUND

    except DataError as error:
        if isinstance(error.orig, InvalidTextRepresentation):
            return jsonify({"msg": "id not found"}), HTTPStatus.BAD_REQUEST
        else:
            raise error

    except werkzeug.exceptions.NotFound as err:
        return jsonify(err.description), HTTPStatus.NOT_FOUND
