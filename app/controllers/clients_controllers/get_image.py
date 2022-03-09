from http import HTTPStatus
from flask import Response
from app.models import Client
from sqlalchemy.orm.exc import NoResultFound
from ipdb import set_trace


def get_image(image_hash: str):
    try:
        client_list: list = [client for client in Client.query.all() if client.image_name == image_hash]
        set_trace()
        if client_list:
            client = client_list[0]
        else:
            raise NoResultFound
        return Response(client.image_bin, mimetype=client.image_mimetype), HTTPStatus.OK
    except NoResultFound:
        return {"msg": "image client not found"}, HTTPStatus.NOT_FOUND
