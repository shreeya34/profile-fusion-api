from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StoreCreate(BaseModel):
    owner_id: int
    name: str
    description: Optional[str] = None
    location: Optional[str] = None
    store_data: Optional[dict] = None

class StoreResponse(StoreCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
