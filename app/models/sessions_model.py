from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class Session(db.Model):

    id: str
    start: str
    end: str
    finished: bool

    __tablename__ = "sessions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    start = Column(DateTime , nullable=False)
    end = Column(DateTime , nullable=False)
    finished = Column(Boolean , default=False)

