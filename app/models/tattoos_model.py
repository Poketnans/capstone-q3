from sqlalchemy import Column, ForeignKey, String, Integer, Text, Boolean
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

@dataclass    
class TattoosModel(db.Model):
    
    id: str
    size: str
    duration: int
    colors: bool
    body_parts: str
    id_client: str
    id_tattooist: str
    id_event: str
        
    __tablename__ = "tattoos"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    size = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    colors = Column(Boolean)
    body_parts = Column(Text)
    id_client = Column(UUID(as_uuid=True), ForeignKey("clients.id"))
    id_tattooist = Column(UUID(as_uuid=True), ForeignKey("tattooists.id"))
    id_event = Column(UUID(as_uuid=True), ForeignKey("events.id"))