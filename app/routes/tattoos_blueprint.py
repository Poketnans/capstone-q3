from flask import Blueprint
from app.controllers.tattoos_controllers import update


bp_tattoos = Blueprint('tattoos', __name__, url_prefix='/tattoos')

bp_tattoos.patch("<id_tattoo>")(update)
