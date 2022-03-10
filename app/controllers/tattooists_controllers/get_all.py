from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import jwt_required

from app.models.tattooists_model import Tattooist


@jwt_required()
def get_all():
    page = request.args.get('page', 1, type=int)
    tattooists = Tattooist.query.paginate(page=page, per_page=15)

    if not tattooists:
        return jsonify([]), HTTPStatus.OK

    return jsonify(tattooists.items), HTTPStatus.OK