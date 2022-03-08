from http import HTTPStatus
from flask import Response

from app.models import Tattooist
from sqlalchemy.orm.exc import NoResultFound

def get_image(image_name:str):
    try:
        tattooists: Tattooist = Tattooist.query.filter_by(image_name=image_name).first()
        if not tattooists:
            raise NoResultFound
        return Response(tattooists.image_bin, mimetype=tattooists.image_mimetype), HTTPStatus.OK
    except NoResultFound:
        return {"msg": "image tattooist not found"}, HTTPStatus.NOT_FOUND