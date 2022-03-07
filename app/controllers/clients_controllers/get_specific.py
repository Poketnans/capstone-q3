from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required


from app.models import Client
import werkzeug


@jwt_required()
def get_specific():
    id = get_jwt_identity().get("id")

    try:
        client = Client.query.filter_by(id=id).first_or_404(
            description={"msg": "client not found"})

    except werkzeug.exceptions.NotFound as err:
        return err.description, HTTPStatus.NOT_FOUND

    return jsonify(client), HTTPStatus.OK
