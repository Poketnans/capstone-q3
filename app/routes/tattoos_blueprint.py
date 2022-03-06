from flask import Blueprint

from app.controllers.tattoos_controllers import get_specific, get_all, update

bp_tattoos = Blueprint('tattoos', __name__, url_prefix='/tattoos')
bp_tattoos.get("/<id_tattoo>")(get_specific) 
bp_tattoos.get("")(get_all)
bp_tattoos.patch("<id_tattoo>")(update)
