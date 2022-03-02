from sqlalchemy import Column, String, Integer, Text, Date
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


@dataclass
class Product(db.Model):

    id: str
    name: str
    quantity: int
    description: str
    validity: str

    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    description = Column(Text)
    validity = Column(Date)
