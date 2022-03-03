from flask import Blueprint
from app.controllers.clients_controllers import post_login

bp = Blueprint("login post", __name__)
bp.post("/clients/login")(post_login)
