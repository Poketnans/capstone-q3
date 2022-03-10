from http import HTTPStatus
from flask import current_app, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
import werkzeug

from app.errors import JSONNotFound, InvalidValueTypesError
from app.models import Client
from app.services import get_files
from app.decorators import validator, verify_payload
import werkzeug.exceptions


@jwt_required()
@validator(password="password", phone="phone", email="email")
@verify_payload(fields_and_types={
                'name': str,
                'email': str,
                'phone': str,
                'password': str,
                'street': str,
                'number': int,
                'city': str,
                'general_information': str,
                }, optional=['name', 'email', 'phone', 'password', 'street', 'number', 'city', 'general_information'])
def update(payload):

    try:
        session: Session = current_app.db.session
        client_jwt = get_jwt_identity()
        id = client_jwt['id']

        client: Client = Client.query.get(id)
        if not client:
            raise NoResultFound

        for key, value in payload.items():
            setattr(client, key, value)

        files = get_files()
        if files:
            for file in files:
                client.image_bin = file.file_bin
                client.image_name = file.filename
                client.image_mimetype = file.mimetype

        session.add(client)
        session.commit()

        return jsonify(client), HTTPStatus.OK
    except JSONNotFound as e:
        return {"msg": f"{e.describe}"}, e.status_code
    except InvalidValueTypesError as err:
        return jsonify(err.description), err.code
    except NoResultFound as e:
        return {"msg": "user not found"}, HTTPStatus.NOT_FOUND
    except werkzeug.exceptions.UnsupportedMediaType as e:
        return e.description, HTTPStatus.UNSUPPORTED_MEDIA_TYPE