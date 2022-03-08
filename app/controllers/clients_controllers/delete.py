from flask import current_app
from flask_jwt_extended import get_jwt_identity, jwt_required

from sqlalchemy.orm import Session
from http import HTTPStatus

from app.models import Client
import werkzeug


@jwt_required()
def delete():
    session: Session = current_app.db.session
    client_jwt = get_jwt_identity()

    try:
        client: Client = Client.query.filter_by(id=client_jwt['id']).first_or_404(
            description={"msg": "client not found"})
        client.password_hash = ""
        session.add(client)
        session.commit()

    except werkzeug.exceptions.NotFound as err:
        return err.description, HTTPStatus.NOT_FOUND

    return "", HTTPStatus.NO_CONTENT
