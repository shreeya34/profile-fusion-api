from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    email: EmailStr
    id: int

    class Config:
        orm_mode = True
        



