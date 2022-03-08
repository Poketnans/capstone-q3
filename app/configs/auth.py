from flask import Flask
from flask_jwt_extended import JWTManager

from app.models import TokenBlocklist


def init_app(app: Flask) -> None:
    ''' Instancia o objeto JWT. '''
    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def if_token_is_revoked(_, jwt_payload):
        jti = jwt_payload["jti"]
        token = TokenBlocklist.query.filter_by(jti=jti).scalar()
        return token is not None
