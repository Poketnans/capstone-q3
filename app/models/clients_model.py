from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import (Column, Date, Integer, LargeBinary, String,
                        Text)
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db
from app.classes.app_with_db import current_app


@dataclass
class Client(db.Model):

    id: str
    name: str
    email: str
    birth_date: str
    phone: str
    general_information: str
    street: str
    number: int
    city: str
    url_image: str = None
    tattoos: list = None

    __tablename__ = "clients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    birth_date = Column(Date, nullable=False)
    password_hash = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    general_information = Column(Text)
    street = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    image_name = Column(String)
    image_bin = Column(LargeBinary)
    image_mimetype = Column(String)

    @property
    def url_image(self):
        return self.url_image
    
    @url_image.getter
    def url_image(self):
        baseUrl = current_app.config["BASE_URL"]
        endpoint = "/client/image/"
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
