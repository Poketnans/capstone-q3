def update():
    ...

#ajustar corretamente para funcionar adquadamente    
from http import HTTPStatus
from flask import jsonify, request
from app.classes.app_with_db import current_app
from flask_jwt_extended import jwt_required , get_jwt_identity
from sqlalchemy.orm import Session
from app.models import Tattooist
from app.decorators import verify_payload
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from app.errors import JSONNotFound
from app.services.get_data_with_images import get_files


@jwt_required()
@verify_payload(
    fields_and_types={
        'name': str,
        'email': str,
        'password': str,
        "general_information": str
    },
    optional=["general_information"]
)
def update(payload):
    try:
        session: Session = current_app.db.session
        tattoist_jwt = get_jwt_identity()
        id = tattoist_jwt['id']

        tattoist: Tattooist = Tattooist.query.get(id)

        for key, value in payload.items():
            setattr(tattoist, key, value)

        files = get_files()
        if files:
            for file in files:
                tattoist.image_bin = file.file_bin
                tattoist.image_name = file.filename
                tattoist.image_mimetype = file.mimetype

        if not payload and not files:
            raise JSONNotFound


        session.add(tattoist)
        session.commit()

        return jsonify(tattoist), HTTPStatus.OK

    except IntegrityError as error:
        if isinstance(error.orig, UniqueViolation):
            message = str(error.orig).split("Key")[1].split("=")[0]
            msg = {"msg": f"{message[2:-1]} already registered, try other"}
            return jsonify(msg), HTTPStatus.CONFLICT
