from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import jwt_required
from app.models.tattoos_model import Tattoo


@jwt_required()
def get_all():
    tattoos = Tattoo.query.all()

    if not tattoos:
        return jsonify([]), HTTPStatus.OK

    return jsonify([{
        "id": tattoo.id,
        "size": tattoo.size,
        "colors": tattoo.colors,
        "body_parts": tattoo.body_parts,
        "tattoo_schedule": tattoo.tattoo_schedule,
        "tattoist": tattoo.tattooist} for tattoo in tattoos
    ]), HTTPStatus.OK
