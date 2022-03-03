from http import HTTPStatus
from flask import request
from flask_jwt_extended import create_access_token
from app.models.clients_model import Client
from datetime import timedelta
from app.services import fixed_values_eval, payload_eval
import werkzeug.exceptions


def post_login() -> dict:
    data = request.get_json()
    try:
        fixed_values_eval.fixed_values_eval(payload_eval.payload_eval(
            data=data,
            email=str,
            password=str,
            optional=[]
        ))

        user = Client.query.filter_by(email=data["email"]).first_or_404(
            description={"msg": "user not found"})

        if not user.check_password(data["password"]):
            return {"msg": "wrong password"}, HTTPStatus.FORBIDDEN

        token = create_access_token(
            identity=user, expires_delta=timedelta(hours=1))

        return {"access token": token}
    except werkzeug.exceptions.NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
    