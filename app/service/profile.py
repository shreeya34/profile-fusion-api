from sqlalchemy.orm import Session
from models import profile

class ProfileService:
    @staticmethod
    def get_profile_by_user_id(db: Session, user_id: int):
        return db.query(profile).filter(profile.user_id == user_id).first()

    @staticmethod
    def create_profile(db: Session, profile_data):
        new_profile = profile(**profile_data)
        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)
        return new_profile
