from http import HTTPStatus

import werkzeug.exceptions
from flask import request
from flask_jwt_extended import create_access_token

from app.errors import FieldMissingError
from app.models.tattooists_model import Tattooist
from app.services import payload_eval


def post_login():
    data = request.get_json()
    try:
        if data == None:
            raise FieldMissingError(description={"msg": "the body was empty"})
        clean_data = payload_eval.payload_eval(
            data=data,
            email=str,
            password=str,
            optional=[]
        )

        user = Tattooist.query.filter_by(email=clean_data["email"]).first_or_404(
            description={"msg": "user not found"})

        if not user.verify_password(clean_data["password"]):
            return {"msg": "wrong password"}, HTTPStatus.FORBIDDEN

        token = create_access_token(
            identity=user)

        return {"access token": token}
    except werkzeug.exceptions.NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
    except FieldMissingError as e:
        return e.description, HTTPStatus.BAD_REQUEST
