from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import jwt_required

from app.models.tattooists_model import Tattooist


@jwt_required()
def get_specific(id_tattooist:str):

    tattoist = Tattooist.query.get(id_tattooist)

    if not tattoist:
        msg = {"error_message":  "Tattooist not found"}
        return jsonify(msg), HTTPStatus.NOT_FOUND

    return jsonify(tattoist), HTTPStatus.OK
