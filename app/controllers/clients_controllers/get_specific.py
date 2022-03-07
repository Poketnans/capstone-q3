from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required


from app.models import Client


@jwt_required()
def get_specific():
    id = get_jwt_identity().get("id")

    client = Client.query.get(id)

    return jsonify(client), HTTPStatus.OK
