from flask import Blueprint

from app.controllers.clients_controllers import post_login, post_create, get_all, get_specific, delete, update, get_image, to_recover_password
from app.controllers.logout import logout

bp_clients = Blueprint("clients", __name__)
bp_clients.post("/clients/login")(post_login)
bp_clients.post("/clients")(post_create)
bp_clients.get("/client")(get_specific)
bp_clients.get("/clients")(get_all)
bp_clients.delete("/clients")(delete)
bp_clients.get("/client/image/<image_hash>")(get_image)
bp_clients.patch("/clients")(update)
bp_clients.patch("/clients")(update)

bp_clients.post("/clients/to_recover")(to_recover_password)
bp_clients.delete("/clients/logout")(logout)