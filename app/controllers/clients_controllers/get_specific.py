from flask import jsonify
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def get_specific():
    client = get_jwt_identity()

    return jsonify(client), HTTPStatus.OK
