from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import jwt_required

from app.models.tattooists_model import Tattooist


@jwt_required()
def get_specific(id_tattooist:str):

    tattoist = Tattooist.query.get(id_tattooist)

    if not tattoist:
        return jsonify([]), HTTPStatus.OK

    return jsonify(tattoist), HTTPStatus.OK
