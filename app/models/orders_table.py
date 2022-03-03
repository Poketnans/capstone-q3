from uuid import uuid4

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db

orders = db.Table('orders',
                  Column('id', UUID(as_uuid=True),
                         primary_key=True, default=uuid4),
                  Column('id_tattoo', UUID(as_uuid=True),
                         ForeignKey('tattoos.id')),
                  )
