from flask import Blueprint
from app.controllers.clients_controllers import post_login

bp_clients = Blueprint("login post", __name__, url_prefix="/clients")
bp_clients.post("/login")(post_login)
