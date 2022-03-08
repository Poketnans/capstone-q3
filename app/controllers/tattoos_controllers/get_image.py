from http import HTTPStatus
from flask import Response

from app.models import TattooImage
from sqlalchemy.orm.exc import NoResultFound


def get_image(image_name: str):
    try:
        tattoo_image: TattooImage = TattooImage.query.filter_by(image_name=image_name).first()
        if not tattoo_image:
            raise NoResultFound
        return Response(tattoo_image.image_bin, mimetype=tattoo_image.image_mimetype), HTTPStatus.OK
    except NoResultFound:
        return {"msg": "image tattooist not found"}, HTTPStatus.NOT_FOUND