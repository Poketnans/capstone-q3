
from http import HTTPStatus
from json import loads

from flask import current_app, jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from werkzeug.utils import secure_filename

from app.errors import FieldMissingError, JSONNotFound
from app.errors.invalid_value_types_error import InvalidValueTypesError
from app.errors.json_not_found import JSONNotFound
from app.models import Tattooist
from app.services import get_data, get_files
from app.services.payload_eval import payload_eval


def post_create():
    try:
        session: Session = current_app.db.session
        data = get_data()

        data_types = {
            "name": str,
            "email": str,
            "password": str,
            "general_information": str,
            "admin": bool
        }

        data = payload_eval(
            data,
            optional=[],
            **data_types
        )

        new_tatooist = Tattooist(**data)

        files = get_files()
        if files:
            for file in files:
                new_tatooist.image_bin = file.file_bin
                new_tatooist.image_name = file.filename
                new_tatooist.image_mimetype = file.mimetype

        session.add(new_tatooist)
        session.commit()

        return jsonify(new_tatooist), HTTPStatus.CREATED

    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            return {"msg": "email already exists"}, e.code
    except InvalidValueTypesError as e:
        return jsonify(e.description), e.code
    except FieldMissingError as e:
        return jsonify(e.description), e.code
    except JSONNotFound as e:
        return {"error": f"{e.describe}"}, e.status_code
