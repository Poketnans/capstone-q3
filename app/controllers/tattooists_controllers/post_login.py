from http import HTTPStatus

import werkzeug.exceptions
from flask_jwt_extended import create_access_token

from app.models.tattooists_model import Tattooist
from app.decorators import verify_payload


@verify_payload(
    fields_and_types={
        "email": str,
        "password": str,
    }
)
def post_login(payload):
    try:
        user = Tattooist.query.filter_by(email=payload["email"]).first_or_404(
            description={"msg": "user not found"})

        if not user.verify_password(payload["password"]):
            return {"msg": "wrong password"}, HTTPStatus.FORBIDDEN

        token = create_access_token(
            identity=user)

        return {"access token": token}, HTTPStatus.OK
    except werkzeug.exceptions.NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
