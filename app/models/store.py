from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from app.db.base import Base
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))  # Assuming a store belongs to a user
    name = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=True)
    location = Column(String, nullable=True)
    store_data = Column(JSONB, nullable=True)  # Extra metadata about the store
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
