from flask import Flask

from .clients_blueprint import bp_clients
from .storage_blueprint import bp_storage
from .tattooists_blueprint import bp_tattooists
from .tattoos_blueprint import bp_tattoos


def init_app(app: Flask) -> None:
    ''' Registra as blueprints '''

    app.register_blueprint(bp_storage)
    app.register_blueprint(bp_tattooists)
    app.register_blueprint(bp_tattoos)
    app.register_blueprint(bp_clients)
