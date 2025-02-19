
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean, Text
from app.db.base import Base
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime 


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    social_links = Column(JSONB)  
    website_link = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)  
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)