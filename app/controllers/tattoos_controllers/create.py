from http import HTTPStatus

from flask import jsonify
from psycopg2.errors import ForeignKeyViolation
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.errors import FieldMissingError, InvalidValueTypesError
from app.classes.app_with_db import current_app

from app.models.tattoos_model import Tattoo
from app.models.sessions_model import Session
from app.models.tattoo_images_model import TattooImage
from app.decorators import verify_payload
from app.services import payload_eval, get_orig_error_field, get_files


@jwt_required()
@verify_payload(
    fields_and_types={
        "size": str,
        "colors": bool,
        "body_parts": str,
        "tattoo_schedule": dict,
        "id_tattooist": str,
    }
)
def create(payload: dict):
    session = current_app.db.session

    user: dict = get_jwt_identity()

    try:
        tattoo_schedule = payload.pop('tattoo_schedule')

        schedule_fields = {"start": str, "end": str, }

        schedule = payload_eval(tattoo_schedule, **schedule_fields)

        new_tattoo = Tattoo(**payload)

        new_session = Session(**schedule)

        new_tattoo.id_client = user.get('id')
        new_tattoo.tattoo_schedule = new_session

        files = get_files()
        if files:
            for file in files:
                image_payload = {
                    "image_bin": file.file_bin,
                    "image_name": file.filename,
                    "image_mimetype": file.mimetype,
                    "id_tattoo": new_tattoo.id
                }

                new_image = TattooImage(**image_payload)

                new_tattoo.image_models.append(new_image)

        session.add(new_tattoo)
        session.commit()
        return jsonify(new_tattoo), HTTPStatus.CREATED

    except InvalidValueTypesError as err:
        return jsonify(err.description), err.code
    except FieldMissingError as err:
        return jsonify(err.description), err.code

    except IntegrityError as error:
        if isinstance(error.orig, ForeignKeyViolation):
            error_field = get_orig_error_field(error)
            msg = {"msg": f"{error_field} not found"}
            return jsonify(msg), HTTPStatus.CONFLICT
        else:
            raise error

