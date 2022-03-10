from flask import Blueprint

from app.controllers.tattoos_controllers import get_specific, get_all, update, create, get_image

bp_tattoos = Blueprint('tattoos', __name__, url_prefix='/tattoos')
bp_tattoos.get("/<id_tattoo>")(get_specific)
bp_tattoos.get("")(get_all)
bp_tattoos.patch("<id_tattoo>")(update)
bp_tattoos.post("")(create)
bp_tattoos.get("/image/<image_hash>")(get_image)
