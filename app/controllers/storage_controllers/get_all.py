from http import HTTPStatus

from flask import jsonify, request

from app.models.storage_model import Storage
from flask_jwt_extended import jwt_required


@jwt_required()
def get_all():
    try:
        page = request.args.get('page', 1, type=int)
        storage = Storage.query.paginate(page=page, per_page=15).items

        serializer = [
            {
                "id": stock.id,
                "name": stock.name,
                "quantity": stock.quantity,
                "validity": stock.validity
            } for stock in storage
        ]

    except AttributeError:
        return jsonify([]), HTTPStatus.OK

    return jsonify(serializer), HTTPStatus.OK
