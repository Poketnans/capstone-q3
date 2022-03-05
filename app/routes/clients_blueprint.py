from flask import Blueprint
from app.controllers.clients_controllers import post_login, post_create, get_all, get_specific, update

bp_clients = Blueprint("clients", __name__, url_prefix="/clients")
bp_clients.post("/login")(post_login)
bp_clients.post("")(post_create)
bp_clients.get("")(get_specific)
bp_clients.get("")(get_all)
bp_clients.patch("")(update)
