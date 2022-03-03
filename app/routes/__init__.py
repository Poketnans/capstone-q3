from flask import Flask
from app.routes.clients_blueprint import bp_clients


def init_app(app: Flask) -> None:
    ''' Registra as blueprints '''

    app.register_blueprint(bp_clients)
    # app.register_blueprint()
