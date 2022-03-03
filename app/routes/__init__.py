from flask import Flask
from app.routes.client_blueprint import bp as client_bp


def init_app(app: Flask) -> None:
    ''' Registra as blueprints '''

    app.register_blueprint(client_bp)
    # app.register_blueprint()
