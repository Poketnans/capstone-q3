from http import HTTPStatus
from flask import Response

from app.models import Client
from sqlalchemy.orm.exc import NoResultFound


def get_image(image_name: str):
    try:
        client: Client = Client.query.filter_by(image_name=image_name).first()
        if not client:
            raise NoResultFound
        return Response(client.image_bin, mimetype=client.image_mimetype), HTTPStatus.OK
    except NoResultFound:
        return {"msg": "image client not found"}, HTTPStatus.NOT_FOUND
