from sqlalchemy import Column, ForeignKey, LargeBinary, String
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


@dataclass
class TattooImage(db.Model):

    id: str
    id_tattoo: str
    image_name: str
    image_bin: str
    iamge_mimetype: str

    __tablename__ = "tattoo_images"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    image_bin = Column(LargeBinary, nullable=False)
    image_name = Column(String, nullable=False)
    iamge_mimetype = Column(String, nullable=False)

    id_tattoo = Column(UUID(as_uuid=True), ForeignKey("tattoos.id"))
