from flask import current_app
from flask_jwt_extended import get_jwt_identity, jwt_required

from sqlalchemy.orm import Session
from http import HTTPStatus

from app.models import Client


@jwt_required()
def delete():
    session: Session = current_app.db.session
    client_jwt = get_jwt_identity()

    client: Client = Client.query.filter_by(id=client_jwt['id']).first()
    client.password_hash = ""
    session.add(client)
    session.commit()

    return "", HTTPStatus.NO_CONTENT