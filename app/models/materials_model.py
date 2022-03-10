from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class Material(db.Model):

    id: str
    id_item: str
    id_tattoo: str
    quantity: int

    __tablename__ = "materials"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    id_item = Column(UUID(as_uuid=True), ForeignKey("storage.id"))
    id_tattoo = Column(UUID(as_uuid=True), ForeignKey("tattoos.id"))
    quantity = Column(Integer)
