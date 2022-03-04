from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Boolean, Column, LargeBinary, String, Text
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class Tattooist(db.Model):

    id: str
    name: str
    email: str
    general_information: str
    admin: str
    url_image: str = None
    
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
    
    @property
    def url_image(self):
        return self.url_image
    
    @url_image.getter
    def url_image(self, text = "http://localhost:5000/tattooists/profile_image/"):
        url = f"{text}{self.image_name}"
        return url    
