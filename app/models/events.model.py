from sqlalchemy import Column, Boolean, Date, DateTime, LargeBinary
from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

@dataclass    
class EventsModel(db.Model):
    
    id: str
    date: str
    start: str
    end: str
    finished: bool
    final_image: str
    
    __tablename__ = "events"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date = Column(Date)
    start = Column(DateTime)
    end = Column(DateTime)
    finished = Column(Boolean)
    final_image = Column(LargeBinary)