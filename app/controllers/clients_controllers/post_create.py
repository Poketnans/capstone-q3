from http import HTTPStatus

from flask import current_app, jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from app.models.clients_model import Client
from app.services.payload_eval import payload_eval


def post_create():
    session = current_app.db.session
    client_data = request.get_json()

    try: 
        field_types = {
            'name': str,
            'email': str,
            'birth_date': str,
            'phone': str,
            'password_hash': str,
            'disclaimer': bool,
            'street': str,
            'number': int,
            'city': str
        }
        
        optional_fields = ["general_information"]
        client_data = payload_eval(client_data, optional_fields , **field_types)
        new_client = Client(**client_data)

        session.add(new_client)
        session.commit()

    except IntegrityError as error:
        if isinstance(error.orig, UniqueViolation):
            return {"error_message": "key value already registered"}, HTTPStatus.CONFLICT
    
    except BadRequest as err:
        return jsonify(err.description), err.code

    except TypeError as err:
        return {"error key": f"key invalid {err}"}, HTTPStatus.BAD_REQUEST
    

    return jsonify(new_client), HTTPStatus.CREATED