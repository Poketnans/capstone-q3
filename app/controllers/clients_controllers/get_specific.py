from flask import jsonify
from app.models import Client
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

from sqlalchemy.orm.exc import NoResultFound


@jwt_required()
def get_specific():
    try:
        client = get_jwt_identity()
        #id = "b3abc756-ef9f-48cf-a538-7a0c34fa3bff"
        #client = Client.query.filter_by(id=id).first()

        return jsonify(client), HTTPStatus.OK
    except Exception as e:
        raise e
