from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.token import Token
from app.db.session import get_db
from app.schemas.user import UserOut,UserCreate
from app.service.user import UserService
from app.core.security import authenticate_user, create_access_token

router = APIRouter(tags=["Authentication"])

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/signup", response_model=UserOut)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)