from app.models.storage_model import Storage
from http import HTTPStatus
from flask import jsonify


def get_all():
    try:
        storage = Storage.query.all()

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
