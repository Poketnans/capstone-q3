from flask import current_app
from flask_jwt_extended import get_jwt_identity, jwt_required

from sqlalchemy.orm import Session
from http import HTTPStatus

from app.models import Tattooist


@jwt_required()
def delete():
    session: Session = current_app.db.session
    tatooist_jwt = get_jwt_identity()

    tattooist: Tattooist = Tattooist.query.filter_by(id=tatooist_jwt['id']).first()
    tattooist.password_hash = ""
    session.add(tattooist)
    session.commit()

    return "", HTTPStatus.NO_CONTENT