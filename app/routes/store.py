from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.store import Store
from app.schemas.store import StoreCreate, StoreResponse

router = APIRouter()

@router.post("/stores/", response_model=StoreResponse)
def create_store(store: StoreCreate, db: Session = Depends(get_db)):
    new_store = Store(**store.dict())
    db.add(new_store)
    db.commit()
    db.refresh(new_store)
    return new_store
