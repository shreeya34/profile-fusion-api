from datetime import datetime  # Correct import
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean, Text
from app.db.base import Base


class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    session_token = Column(String, unique=True, index=True)
    expires_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)