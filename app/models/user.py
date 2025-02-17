from datetime import datetime 
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean, Text
from app.db.base import Base
import uuid

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    username = Column(String, unique=True, index=True, nullable=False, default=lambda: f"user_{uuid.uuid4().hex[:8]}")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    

   
    


  
    

  