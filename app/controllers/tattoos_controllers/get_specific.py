from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import jwt_required
import werkzeug.exceptions
from app.models.tattoos_model import Tattoo
from app.models.sessions_model import Session
from app.models.tattooists_model import Tattooist
from sqlalchemy.exc import DataError


@jwt_required()
def get_specific(id_tattoo):
    try:
        tattoo = Tattoo.query.get_or_404(id_tattoo, description={"msg": "tattoo not found"})

        return jsonify({
            "id": tattoo.id,
            "size": tattoo.size,
            "colors": tattoo.colors,
            "body_parts": tattoo.body_parts,
            "tattoo_schedule": {
                        "start": Session.query.get(tattoo.id_session).start,
                        "end": Session.query.get(tattoo.id_session).end,
                        "finished": Session.query.get(tattoo.id_session).finished,
                        },
            "tattoist": {
                "name": Tattooist.query.get(tattoo.id_tattooist).name,
                "email": Tattooist.query.get(tattoo.id_tattooist).email,
                "image": Tattooist.query.get(tattoo.id_tattooist).url_image
            }}
        ), HTTPStatus.OK
    except werkzeug.exceptions.NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
    except DataError:
        return {"msg": "wrong id format"}, HTTPStatus.BAD_REQUEST