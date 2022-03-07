from http import HTTPStatus

from flask import jsonify
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.classes.app_with_db import current_app
from app.models.clients_model import Client
from app.decorators import verify_payload
from app.services.get_data_with_images import get_files


@verify_payload(
    fields_and_types={
        'name': str,
        'email': str,
        'password': str,
        'birth_date': str,
        'phone': str,
        "general_information": str,
        'street': str,
        'number': int,
        'city': str
    },
    optional=["general_information"]
)
def post_create(payload):
    session: Session = current_app.db.session

    try:
        new_client = Client(**payload)

        files = get_files()
        if files:
            for file in files:
                new_client.image_bin = file.file_bin
                new_client.image_name = file.filename
                new_client.image_mimetype = file.mimetype

        session.add(new_client)
        session.commit()

    except IntegrityError as error:
        if isinstance(error.orig, UniqueViolation):
            message = str(error.orig).split("Key")[1].split("=")[0]
            msg = {"msg": f"{message[2:-1]} already registered"}
            return jsonify(msg), HTTPStatus.CONFLICT

    return jsonify(new_client), HTTPStatus.CREATED
