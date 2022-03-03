from flask import Flask

from .clients_blueprint import bp_clients
from .orders_blueprint import bp_orders
from .products_blueprint import bp_products
from .tattooists_blueprint import bp_tattooists
from .tattoos_blueprint import bp_tattoos


def init_app(app: Flask) -> None:
    ''' Registra as blueprints '''

    app.register_blueprint(bp_clients)
    app.register_blueprint(bp_orders)
    app.register_blueprint(bp_products)
    app.register_blueprint(bp_tattooists)
    app.register_blueprint(bp_tattoos)
