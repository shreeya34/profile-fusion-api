
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean, Text
from app.db.base import Base
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime 


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    platform = Column(String, index=True)
    platform_id = Column(String, index=True)
    username = Column(String, index=True)
    profile_data = Column(JSONB)  # For storing profile details as JSON
    social_links = Column(JSONB)  # For storing social media links as JSON
    created_at = Column(DateTime, default=datetime.utcnow)  # Correct usage
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)