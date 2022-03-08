from flask import current_app, redirect
from flask_jwt_extended import get_jwt_identity, jwt_required

from sqlalchemy.orm import Session
from http import HTTPStatus

from app.models import Tattooist
import werkzeug


@jwt_required()
def delete():
    session: Session = current_app.db.session

    try:
        tattoist_jwt = get_jwt_identity()
        id = tattoist_jwt['id']

        tattooist: Tattooist = session.query(Tattooist).filter_by(id=id).first_or_404(
            description={"msg": "tattooist not found"})
        tattooist.password_hash = ""
        session.add(tattooist)
        session.commit()

    except werkzeug.exceptions.NotFound as err:
        return err.description, HTTPStatus.NOT_FOUND

    return redirect("/tattooists/logout")
