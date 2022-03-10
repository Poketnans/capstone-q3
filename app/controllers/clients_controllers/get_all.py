from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import jwt_required

from app.models.clients_model import Client

@jwt_required()
def get_all():
    page = request.args.get('page', 1, type=int)
    clients = Client.query.paginate(page=page, per_page=15)
    if not clients:
        return jsonify([]), HTTPStatus.OK

    return jsonify(clients.items), HTTPStatus.OK
