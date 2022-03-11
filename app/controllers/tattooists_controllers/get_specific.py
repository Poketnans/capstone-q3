from http import HTTPStatus
from pydoc import describe

from flask import jsonify
from flask_jwt_extended import jwt_required
import werkzeug

from app.models.tattooists_model import Tattooist
from sqlalchemy.exc import DataError


@jwt_required()
def get_specific(id_tattooist: str):

    try:
        tattoist = Tattooist.query.get_or_404(
            id_tattooist, description={"msg": "tattoist not found"})

        if not tattoist:
            msg = {"msg": "not found"}
            return jsonify(msg), HTTPStatus.NOT_FOUND

    except DataError:
        return {"msg": "wrong id format"}, HTTPStatus.BAD_REQUEST
    except werkzeug.exceptions.NotFound as err:
        return err.description, HTTPStatus.NOT_FOUND

    return jsonify(tattoist), HTTPStatus.OK
