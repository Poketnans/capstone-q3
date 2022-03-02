from app.configs.database import db
from sqlalchemy import Column, ForeignKey
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

orders = db.Table('orders',
                  Column('id', UUID(as_uuid=True),
                         primary_key=True, default=uuid4),
                  Column('id_tattoo', UUID(as_uuid=True),
                         ForeignKey('tattoos.id')),
                  )
