from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required


@jwt_required()
def get_specific():
    client = get_jwt_identity()

    return jsonify(client), HTTPStatus.OK
