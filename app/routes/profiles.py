from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.session import get_db
from app.models.profile import Profile
from app.schemas.profiles import ProfileCreate, ProfileUpdate, ProfileResponse

router = APIRouter()

# Helper function to get a profile or raise 404
def get_profile_or_404(profile_id: int, db: Session):
    db_profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile

# Create a social media profile
@router.post("/profiles/", response_model=ProfileResponse)
def create_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    """
    Create a new social media links profile.
    """
    db_profile = Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

# List all social media profiles
@router.get("/profiles/", response_model=List[ProfileResponse])
def list_profiles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    List all social media profiles with pagination.
    """
    profiles = db.query(Profile).offset(skip).limit(limit).all()
    return profiles

# Get a specific social media profile by ID
@router.get("/profiles/{profile_id}", response_model=ProfileResponse)
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific social media profile by its ID.
    """
    return get_profile_or_404(profile_id, db)

# Update a social media profile
@router.put("/profiles/{profile_id}", response_model=ProfileResponse)
def update_profile(profile_id: int, profile: ProfileUpdate, db: Session = Depends(get_db)):
    """
    Update a specific social media profile by its ID.
    Only the provided fields will be updated.
    """
    db_profile = get_profile_or_404(profile_id, db)
    for key, value in profile.dict(exclude_unset=True).items():
        setattr(db_profile, key, value)
    db.commit()
    db.refresh(db_profile)
    return db_profile

# Delete a social media profile
@router.delete("/profiles/{profile_id}")
def delete_profile(profile_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific social media profile by its ID.
    """
    db_profile = get_profile_or_404(profile_id, db)
    db.delete(db_profile)
    db.commit()
    return {"message": "Profile deleted successfully"}