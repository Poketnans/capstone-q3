from http import HTTPStatus
from flask import Response

from app.models import Tattooist
from sqlalchemy.orm.exc import NoResultFound


def get_image(image_hash: str):
    try:
        tattooist_list: list(Tattooist) = [tattooist for tattooist in Tattooist.query.all(
        ) if tattooist.image_hash == image_hash]
        if tattooist_list:
            tattooist = tattooist_list[0]
        else:
            raise NoResultFound
        return Response(tattooist.image_bin, mimetype=tattooist.image_mimetype), HTTPStatus.OK
    except NoResultFound:
        return {"msg": "image tattooist not found"}, HTTPStatus.NOT_FOUND
