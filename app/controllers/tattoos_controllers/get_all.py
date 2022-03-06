from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import jwt_required
from app.models.tattoos_model import Tattoo


@jwt_required()
def get_all():
    tattoos = Tattoo.query.all()

    if not tattoos:
        return jsonify([]), HTTPStatus.OK

    return jsonify(tattoos), HTTPStatus.OK
