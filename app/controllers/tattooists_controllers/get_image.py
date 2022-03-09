from http import HTTPStatus
from flask import Response

from app.models import Tattooist
from sqlalchemy.orm.exc import NoResultFound


def get_image(image_hash: str):
    try:
        tattooist = Tattooist.query.filter_by(image_name = image_hash).first()
        if not tattooist:
            raise NoResultFound
        return Response(tattooist.image_bin, mimetype=tattooist.image_mimetype), HTTPStatus.OK
    except NoResultFound:
        return {"msg": "image tattooist not found"}, HTTPStatus.NOT_FOUND
