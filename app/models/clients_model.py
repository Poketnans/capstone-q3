from sqlalchemy import Column, String, Integer, Text, Boolean, Date, LargeBinary
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class Client(db.Model):
    
    id: str
    name: str
    email: str
    birth_date: str
    phone: str
    general_information: str
    disclaimer: bool
    street: str
    number: int
    city: str
    image: str
    
    __tablename__ = "clients"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    birth_date = Column(Date, nullable = False)
    password_hash = Column(String, nullable = False, unique = True)
    phone = Column(String, nullable = False, unique = True)
    general_information = Column(Text)
    disclaimer = Column(Boolean)
    street = Column(String, nullable = False)
    number = Column(Integer, nullable = False)
    city = Column(String, nullable = False)
    image = Column(LargeBinary)