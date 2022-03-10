from http import HTTPStatus
from flask import jsonify
from app.classes.app_with_db import current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm import Session
from app.models import Tattooist
from psycopg2.errors import UniqueViolation, ForeignKeyViolation
from app.decorators import verify_payload, validator
from sqlalchemy.exc import IntegrityError
from app.services import get_files, get_orig_error_field
import werkzeug.exceptions


@jwt_required()
@validator(email="email", password="password")
@verify_payload(
    fields_and_types={
        'name': str,
        'email': str,
        'password': str,
        "general_information": str
    },
    optional=["general_information", "name", "email", "password"]
)
def update(payload):
    try:
        session: Session = current_app.db.session
        tattoist_jwt = get_jwt_identity()
        id = tattoist_jwt['id']

        tattoist: Tattooist = session.query(Tattooist).filter_by(id=id).first_or_404(
            description={"msg": "tattooist not found"})

        for key, value in payload.items():
            setattr(tattoist, key, value)

        files = get_files()
        if files:
            for file in files:
                tattoist.image_bin = file.file_bin
                tattoist.image_name = file.filename
                tattoist.image_mimetype = file.mimetype

        session.add(tattoist)
        session.commit()

        return jsonify(tattoist), HTTPStatus.OK

    except IntegrityError as error:
        if isinstance(error.orig, UniqueViolation):
            error_field = get_orig_error_field(error)
            msg = {"msg": f"{error_field} already registered"}
            return jsonify(msg), HTTPStatus.CONFLICT
        elif isinstance(error.orig, ForeignKeyViolation):
            error_field = get_orig_error_field(error)
            msg = {"msg": f"{error_field} not found"}
            return jsonify(msg), HTTPStatus.CONFLICT
        else:
            raise error
    except werkzeug.exceptions.NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
    except werkzeug.exceptions.UnsupportedMediaType as e:
        return e.description, HTTPStatus.UNSUPPORTED_MEDIA_TYPE