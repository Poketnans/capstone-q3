from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import jwt_required

from app.models.clients_model import Client


@jwt_required()
def get_all():

    clients = Client.query.all()

    if not clients:
        return jsonify([]), HTTPStatus.OK

    return jsonify(clients), HTTPStatus.OK
