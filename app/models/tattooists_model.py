from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
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
    image_hash = None
    image_name: str = None

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
        endpoint = "/tattooists/image/"
        url = f"{baseUrl}{endpoint}{self.image_name}"
        return url

    @property
    def password(self):
        raise AttributeError('password cannot be accessed')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    def list_sessions(self):
        list_tattoo_schedule = []
        date_now = datetime.utcnow() - timedelta(hours=3)

        for element in self.tattoos:
            start = element.tattoo_schedule.start
            if(start >= date_now):
                list_tattoo_schedule.append(element.tattoo_schedule)
        return list_tattoo_schedule

    @property
    def image_hash(self):
        return self.image_name

    @image_hash.setter
    def image_hash(self, image_name_to_hash):
        hash = hashlib.md5(
            f"{image_name_to_hash}{self.email}".encode()).hexdigest()
        self.image_name = hash
