from http import HTTPStatus
from flask import Response

from app.models import TattooImage
from sqlalchemy.orm.exc import NoResultFound


def get_image(image_hash: str):
    try:
        tattoo_list = [tattoo for tattoo in TattooImage.query.all(
        ) if tattoo.image_hash == image_hash]
        if tattoo_list:
            tattoo_image = tattoo_list[0]
        else:
            raise NoResultFound
        return Response(tattoo_image.image_bin, mimetype=tattoo_image.image_mimetype), HTTPStatus.OK
    except NoResultFound:
        return {"msg": "image tattoo not found"}, HTTPStatus.NOT_FOUND
