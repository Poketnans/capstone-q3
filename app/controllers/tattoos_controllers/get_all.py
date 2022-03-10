from http import HTTPStatus
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.models.tattoos_model import Tattoo


@jwt_required()
def get_all():
    page = request.args.get('page', 1, type=int)
    tattoos = Tattoo.query.paginate(page=page, per_page=15)

    if not tattoos:
        return jsonify([]), HTTPStatus.OK

    return jsonify(tattoos.items), HTTPStatus.OK
