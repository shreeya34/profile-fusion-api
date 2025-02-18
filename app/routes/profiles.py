from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.service.profile import ProfileService
from app.schemas.profiles import ProfileCreate
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/profile")
async def create_profile(profile: ProfileCreate, user_id: int, db: Session = Depends(get_db)):
    try:
        existing_profile = ProfileService.get_profile_by_user_id(db, user_id)
        if existing_profile:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Profile already exists")

        created_profile = ProfileService.create_profile(db, user_id, profile)

        return {"success": True, "message": "Profile created successfully", "profile": created_profile}

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": str(e)}
        )
