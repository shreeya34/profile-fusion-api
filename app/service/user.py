from fastapi import Depends, HTTPException, status
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash
from sqlalchemy.orm import Session
from fastapi import APIRouter

router = APIRouter()

# app/services/user_service.py
class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCreate):
        try:
            db_user = db.query(User).filter(User.email == user.email).first()
            if db_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered"
                )
            hashed_password = get_password_hash(user.password)
            new_user = User(email=user.email, hashed_password=hashed_password)
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        except Exception as e:
            db.rollback()
            print(f"Error creating user: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An error occurred while creating the user"
            )

# app/api/endpoints/user.py
@router.post("/register/", status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)