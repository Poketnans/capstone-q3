from sqlalchemy import Column, String, Text, Boolean, LargeBinary
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class Tattooists(db.Model):
    
    id: str
    name: str
    email: str
    image: str
    general_information: str
    admin: str
        
    __tablename__ = "tattooists"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    password_hash = Column(String, nullable = False, unique = True)
    image = Column(LargeBinary, nullable = False)
    general_information = Column(Text)
    admin = Column(Boolean)