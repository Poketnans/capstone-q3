from flask import Blueprint
from app.controllers.tattoos_controllers import get_specific

bp_tattoos = Blueprint('tattoos', __name__, url_prefix='/tattoos')
bp_tattoos.get("/<string:id_tattoo>")(get_specific) 
