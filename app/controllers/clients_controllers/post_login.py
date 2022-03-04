from http import HTTPStatus
#from ipdb import set_trace
from flask import request
from flask_jwt_extended import create_access_token
from app.models.clients_model import Client
from app.services import payload_eval
import werkzeug.exceptions
from app.configs import Config
from app.errors import FieldMissingError


def post_login():
    data = request.get_json()
    # set_trace()
    try:
        if data == None:
            raise FieldMissingError(description={"msg": "the body was empty"})

        clean_data = payload_eval.payload_eval(
            data=data,
            email=str,
            password=str,
            optional=[]
        )

        user = Client.query.filter_by(email=clean_data["email"]).first_or_404(
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
