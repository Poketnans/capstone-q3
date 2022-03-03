from http import HTTPStatus
from flask import request
from flask_jwt_extended import create_access_token
from app.models.clients_model import Client
from app.services import payload_eval
import werkzeug.exceptions
from app.configs import Config

def post_login():
    data = request.get_json()
    try:
        clean_data = payload_eval.payload_eval(
            data=data,
            email=str,
            password=str,
            optional=[]
        )
        
        user = Client.query.filter_by(email=clean_data["email"]).first_or_404(
            description={"msg": "user not found"})

        if not user.check_password(clean_data["password"]):
            return {"msg": "wrong password"}, HTTPStatus.FORBIDDEN

        token = create_access_token(
            identity=user, expires_delta=Config.JWT_ACCESS_TOKEN_EXPIRES)

        return {"access token": token}
    except werkzeug.exceptions.NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND