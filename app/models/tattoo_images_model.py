from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, LargeBinary, String
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class TattooImage(db.Model):

    id: str
    id_tattoo: str
    url_image: str = None

    __tablename__ = "tattoo_images"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    image_bin = Column(LargeBinary, nullable=False)
    image_name = Column(String, nullable=False)
    image_mimetype = Column(String, nullable=False)

    id_tattoo = Column(UUID(as_uuid=True), ForeignKey("tattoos.id"))
    
    @property
    def url_image(self):
        return self.url_image

    @url_image.getter
    def url_image(self, text="http://localhost:5000/tattoo/image/"):
        url = f"{text}{self.image_name}"
        return url
