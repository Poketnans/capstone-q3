
from http import HTTPStatus
from flask import current_app

from sqlalchemy.orm import Session

from app.errors import NotAnAdmin
from app.models import Tattooist
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.decorators import verify_payload, validator

from app.models.tattooists_model import Tattooist


@jwt_required()
@validator(password="new_password")
@verify_payload(
    fields_and_types={
        'new_password': str,
        "id": str,
    },
)
def to_recover_password(payload):
    try:
        id = get_jwt_identity().get("id")

        tatooist: Tattooist = Tattooist.query.get(id)
        if not tatooist.admin:
            raise NotAnAdmin

        session: Session = current_app.db.session
        tattoist: Tattooist = Tattooist.query.get(payload['id'])
        tattoist.password = payload['new_password']
        session.commit()

        return "", HTTPStatus.NO_CONTENT
    except NotAnAdmin as e:
        return {"msg": "not unauthorized"}, HTTPStatus.UNAUTHORIZED
