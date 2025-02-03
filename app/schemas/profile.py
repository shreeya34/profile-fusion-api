from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict

# Base model for common fields
class ProfileBase(BaseModel):
    platform: str
    platform_id: str
    username: str
    profile_data: Dict  
    social_links: Dict

# Model for creating a profile
class ProfileCreate(ProfileBase):
    user_id: int  # Required for creating a profile

class ProfileUpdate(BaseModel):
    platform: Optional[str] = None
    platform_id: Optional[str] = None
    username: Optional[str] = None
    profile_data: Optional[Dict] = None
    social_links: Optional[Dict] = None

# Model for API responses
class ProfileResponse(ProfileBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Enable ORM mode for SQLAlchemy compatibility