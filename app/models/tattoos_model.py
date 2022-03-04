from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref

from app.configs.database import db


@dataclass
class Tattoo(db.Model):

    id: str
    size: str
    colors: bool
    body_parts: str
    id_client: str
    id_tattooist: str
    id_session: str

    __tablename__ = "tattoos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    size = Column(String, nullable=False)
    colors = Column(Boolean, nullable=False)
    body_parts = Column(Text)
    id_client = Column(UUID(as_uuid=True), ForeignKey("clients.id"))
    id_tattooist = Column(UUID(as_uuid=True), ForeignKey("tattooists.id"))
    id_session = Column(UUID(as_uuid=True), ForeignKey("sessions.id"))

    image_models = relationship("TattooImage", uselist=True)

    # client = relationship("Client", backref=backref(
    #    "tattoos", uselist=True), uselist=False)

    tattooist = relationship("Tattooist", backref=backref(
        "tattoos", uselist=True), uselist=False)

    tattoo_schedule = relationship("Session", uselist=False)
    materials = relationship("Material", uselist=True)
