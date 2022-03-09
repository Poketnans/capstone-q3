from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Boolean, Column, LargeBinary, String, Text
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db
from app.classes.app_with_db import current_app
import hashlib


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
    password_hash = Column(String, nullable=False)
    general_information = Column(Text)
    admin = Column(Boolean)
    image_name = Column(String)
    image_bin = Column(LargeBinary)
    image_mimetype = Column(String)

    @property
    def url_image(self):
        return self.url_image

    @url_image.getter
    def url_image(self):
        baseUrl = current_app.config["BASE_URL"]
        endpoint = "/tatooists/image/"
        url = f"{baseUrl}{endpoint}{self.image_hash}"
        return url

    @property
    def password(self):
        raise AttributeError('password cannot be accessed')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    @property
    def image_hash(self):
        return self.image_hash

    @image_hash.getter
    def image_hash(self):
        return hashlib.md5(f"{self.image_name}{self.id}".encode()).hexdigest()