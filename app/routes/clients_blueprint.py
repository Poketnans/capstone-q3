from flask import Blueprint
from app.controllers.clients_controllers import post_create

bp_clients = Blueprint('clients', __name__, url_prefix='/clients')

bp_clients.post("")(post_create)