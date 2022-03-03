from sqlalchemy import (
    Column, String, Text, Boolean, LargeBinary
)
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


@dataclass
class Tattooist(db.Model):

    id: str
    name: str
    email: str
    general_information: str
    admin: str
    image_name: str
    image_bin: str
    image_mimetype: str

    __tablename__ = "tattooists"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False, unique=True)
    general_information = Column(Text)
    admin = Column(Boolean)
    image_name = Column(String)
    image_bin = Column(LargeBinary)
    image_mimetype = Column(String)
    
    
