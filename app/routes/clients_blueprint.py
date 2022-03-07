from flask import Blueprint

from app.controllers.clients_controllers import (get_all, get_specific,
                                                 post_create, post_login)

bp_clients = Blueprint("clients", __name__, url_prefix="/")
bp_clients.post("clients/login")(post_login)
bp_clients.post("clients")(post_create)
bp_clients.get("client")(get_specific)
bp_clients.get("clients")(get_all)
