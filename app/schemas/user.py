from pydantic import BaseModel, EmailStr, validator
import uuid

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    username: str = None  

    @validator("username", pre=True, always=True)
    def set_default_username(cls, v):
        return v or f"user_{uuid.uuid4().hex[:8]}"  # Auto-generate if missing

class UserOut(BaseModel):
    email: EmailStr
    id: int

    class Config:
        orm_mode = True
        



