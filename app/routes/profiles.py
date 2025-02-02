from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.db.session import get_db
from app.models.profile import Profile
from pydantic import BaseModel

router = APIRouter()

# Pydantic models for request/response
class ProfileBase(BaseModel):
    platform: str
    platform_id: str
    username: str
    profile_data: dict
    social_links: dict

class ProfileCreate(ProfileBase):
    user_id: int

class ProfileUpdate(ProfileBase):
    pass

class ProfileResponse(ProfileBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True