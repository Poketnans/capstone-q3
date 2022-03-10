import werkzeug

from http import HTTPStatus
from flask import Response

from app.models import TattooImage


def get_image(image_hash: str):
    try:
        tattoo_image = TattooImage.query.filter_by(image_name=image_hash).first_or_404(
            description={"msg": "image not found"})
        return Response(tattoo_image.image_bin, mimetype=tattoo_image.image_mimetype), HTTPStatus.OK
    except werkzeug.exceptions.NotFound as err:
        return err.description, HTTPStatus.NOT_FOUND
