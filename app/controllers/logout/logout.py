from http import HTTPStatus
from flask import current_app, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from datetime import datetime, timezone

from app.models import TokenBlocklist
from sqlalchemy.orm import Session


@jwt_required()
def logout():
    session: Session = current_app.db.session
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)
    token_revoked = TokenBlocklist(jti=jti, created_at=now)

    session.add(token_revoked)
    session.commit()
    return jsonify(msg="JWT revoked"), HTTPStatus.OK
