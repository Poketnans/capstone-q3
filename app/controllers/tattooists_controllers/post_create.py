
from http import HTTPStatus

from flask import current_app, jsonify
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models import Tattooist
from app.services import get_files
from app.decorators import verify_payload, validator


@validator(email="email", password="password")
@verify_payload(
    fields_and_types={
        "name": str,
        "email": str,
        "password": str,
        "general_information": str,
        "admin": bool
    },
    optional=["general_information"]
)
def post_create(payload):
    try:
        session: Session = current_app.db.session

        new_tatooist = Tattooist(**payload)

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
