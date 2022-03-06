from http import HTTPStatus, client

from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from pytest import Session
from sqlalchemy.exc import IntegrityError

from app.classes.app_with_db import current_app
from app.errors import FieldMissingError, InvalidValueTypesError
from app.services.get_data_with_images import get_data_with_images, get_files
from app.models.clients_model import Client
from app.services.payload_eval import payload_eval


def post_create():
    session: Session = current_app.db.session
    client_data = get_data_with_images()

    try: 
        field_types = {
            'name': str,
            'email': str,
            'birth_date': str,
            'phone': str,
            'password': str,
            'street': str,
            'number': int,
            'city': str
        }
        
        optional_fields = ["general_information" ,"image_name","image_bin","image_mimetype", "tattoos"]
        client_data = payload_eval(client_data, optional_fields , **field_types)
        new_client = Client(**client_data)

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
    
    except FieldMissingError as err:
        return jsonify(err.description),err.code

    except InvalidValueTypesError as err:
        return jsonify(err.description),err.code
    
    return jsonify(new_client), HTTPStatus.CREATED
