from http import HTTPStatus
from flask import Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Client
from sqlalchemy.orm.exc import NoResultFound


@jwt_required()
def get_image():
    try:
        client_jwt = get_jwt_identity()
        id = client_jwt['id']
        client: Client = Client.query.get(id)
        if not client:
            raise NoResultFound
        return Response(client.image_bin, mimetype=client.image_mimetype), HTTPStatus.OK
    except NoResultFound:
        return {"msg": "client not found"}, HTTPStatus.NOT_FOUND
