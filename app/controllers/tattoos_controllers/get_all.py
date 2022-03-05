from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import jwt_required
from app.models.tattoos_model import Tattoo
from app.models.sessions_model import Session
from app.models.tattooists_model import Tattooist


@jwt_required()
def get_all():
    tattoos = Tattoo.query.all()

    if not tattoos:
        return jsonify([]), HTTPStatus.OK

    return jsonify([{
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
                "image": Tattooist.query.get(tattoo.id_tattooist).image_bin
        }} for tattoo in tattoos
    ]), HTTPStatus.OK
