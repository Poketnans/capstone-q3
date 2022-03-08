from dataclasses import dataclass
import datetime
from email.policy import default
from app.configs.database import db


@dataclass
class TokenBlocklist(db.Model):

    id: str
    jti: str
    created_at: str

    __tablename__ = "token_blocklist"

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow())
