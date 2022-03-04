from http import HTTPStatus

from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from app.models.clients_model import Client
from app.classes.app_with_db import current_app
from app.services.payload_eval import payload_eval
from app.errors import InvalidValueTypesError , FieldMissingError

def post_create():
    session = current_app.db.session
    client_data = request.get_json()

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

        session.add(new_client)
        session.commit()

    except IntegrityError as error:
        if isinstance(error.orig, UniqueViolation):
            msg = {"error_message": "key value already registered"}
            return jsonify(msg), HTTPStatus.CONFLICT
    
    except FieldMissingError as err:
        return jsonify(err.description),err.code

    except InvalidValueTypesError as err:
        return jsonify(err.description),err.code
    
    return jsonify(new_client), HTTPStatus.CREATED