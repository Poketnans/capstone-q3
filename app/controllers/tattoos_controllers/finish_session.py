from http import HTTPStatus
from flask import jsonify
import werkzeug
from app.models import Tattoo, Session
from app.classes.app_with_db import current_app

from sqlalchemy.exc import DataError


def finish_session(id_tattoo):

    session = current_app.db.session

    try:

        tattoo = Tattoo.query.get_or_404(
            id_tattoo, description={"msg": "tattoo not found"})

        tattoo_schedule: Session = tattoo.tattoo_schedule

        tattoo_schedule.finished = True

        tattoo = Tattoo.query.get_or_404(
            id_tattoo, description={"msg": "tattoo not found"})

        session.commit()

    except werkzeug.exceptions.NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
    except DataError:
        return {"msg": "wrong id format"}, HTTPStatus.BAD_REQUEST

    return jsonify(tattoo), HTTPStatus.OK
