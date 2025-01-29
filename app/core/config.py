# app/core/config.py
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"

settings = Settings()
DATABASE_URL = str(settings.DATABASE_URL)
