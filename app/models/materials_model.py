from sqlalchemy import Column, Integer, ForeignKey
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class Materials(db.Model):
    
    id: str
    id_order: str
    id_product: str
    quantity: int
    
    __tablename__ = "clients"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    id_order = Column(UUID(as_uuid=True), ForeignKey("orders.id"))
    id_product = Column(UUID(as_uuid=True), ForeignKey("products.id"))
    quantity = Column(Integer)