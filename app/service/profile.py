from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.schemas.profiles import ProfileCreate

class ProfileService:
    @staticmethod
    def create_profile(db: Session, user_id: int, profile_data: ProfileCreate):
        new_profile = Profile(
            user_id=user_id,
            first_name=profile_data.first_name,
            last_name=profile_data.last_name,
            social_links=profile_data.social_links,
            website_link=profile_data.website_link,
        )
        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)
        return new_profile
    
    @staticmethod
    def get_profile_by_user_id(db: Session, user_id: int):
        return db.query(Profile).filter(Profile.user_id == user_id).first()
