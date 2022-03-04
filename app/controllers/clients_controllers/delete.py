from flask_jwt_extended import get_jwt_identity
from sqlalchemy.orm.exc import NoResultFound

from app.models import Client


def delete():
    ...
    try:
        client_jwt = get_jwt_identity()

        client = Client.query.filter_by(id=client_jwt['id']).first()

    except NoResultFound:
        return {"error": ""}
