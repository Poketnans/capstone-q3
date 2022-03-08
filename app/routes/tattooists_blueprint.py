from flask import Blueprint

from app.controllers import tattooists_controllers

bp_tattooists = Blueprint('tattooists', __name__, url_prefix='/tattooists')

bp_tattooists.post("")(tattooists_controllers.post_create)
bp_tattooists.post("/login")(tattooists_controllers.post_login)
bp_tattooists.get("/<id_tattooist>")(tattooists_controllers.get_specific)
bp_tattooists.get("")(tattooists_controllers.get_all)
bp_tattooists.patch("")(tattooists_controllers.update)
bp_tattooists.delete("")(tattooists_controllers.delete)
bp_tattooists.get("/image/<image_hash>")(tattooists_controllers.get_image)