from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import jwt_required

from app.models.tattooists_model import Tattooist


@jwt_required()
def get_all():

    tattooists = Tattooist.query.all()

    if not tattooists:
        return jsonify([]), HTTPStatus.OK

    return jsonify(tattooists), HTTPStatus.OK