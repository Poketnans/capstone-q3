from flask import Flask

#from .orders_blueprint import bp_orders
from .storage_blueprint import bp_storage
from .tattooists_blueprint import bp_tattooists
from .tattoos_blueprint import bp_tattoos
from .clients_blueprint import bp_clients


def init_app(app: Flask) -> None:
    ''' Registra as blueprints '''

    # app.register_blueprint(bp_orders)
    app.register_blueprint(bp_storage)
    app.register_blueprint(bp_tattooists)
    app.register_blueprint(bp_tattoos)
    app.register_blueprint(bp_clients)
