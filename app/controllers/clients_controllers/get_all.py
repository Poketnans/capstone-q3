from http import HTTPStatus
from flask import jsonify

from app.models.clients_model import Client

def get_all():
    
    clients = Client.query.all()
    
    if not clients:
        return jsonify([]), HTTPStatus.OK
    
    return jsonify(clients), HTTPStatus.OK
