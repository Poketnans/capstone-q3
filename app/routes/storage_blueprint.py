from flask import Blueprint
from app.controllers.storage_controllers import get_all, create, update

bp_storage = Blueprint('storage', __name__, url_prefix='/storage')

bp_storage.get("")(get_all)
bp_storage.post("")(create)
bp_storage.patch("/<id>")(update)
