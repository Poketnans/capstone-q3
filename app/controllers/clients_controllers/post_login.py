from http import HTTPStatus

import werkzeug.exceptions
from flask_jwt_extended import create_access_token

from app.errors import FieldMissingError
from app.models.clients_model import Client
from app.decorators.verify_payload import verify_payload


@verify_payload(
    fields_and_types = {
        "email":str,
        "password":str
        },
    optional=[])
def post_login(payload):
    try:
        user = Client.query.filter_by(email=payload["email"]).first_or_404(
            description={"msg": "user not found"})

        if not user.verify_password(payload["password"]):
            return {"msg": "wrong password"}, HTTPStatus.FORBIDDEN

        token = create_access_token(
            identity={"id": user.id})

        return {"access token": token}
    except werkzeug.exceptions.NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
    
