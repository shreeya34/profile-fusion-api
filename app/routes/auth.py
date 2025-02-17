import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
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

@router.post("/signup")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user.username = user.username or f"user_{uuid.uuid4().hex[:8]}"

        while UserService.get_user_by_username(db, user.username):
            user.username = f"user_{uuid.uuid4().hex[:8]}"  # Generate another one

        if UserService.get_user_by_email(db, user.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

        created_user = UserService.create_user(db, user)

        return {"success": True, "message": "User created successfully", "user": created_user}

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": str(e)}
        )


@router.get("/exists",tags=['users'])
async def link_exists(username:str,db:Session=Depends(get_db)):
    user=UserService.get_user_by_username(db,username)
    if user:
        return {"success":False,"message":"Username already exists"}
    return {"success":True,"message":f"Username {username} is available"}
    