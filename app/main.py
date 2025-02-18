from fastapi import APIRouter, FastAPI
from dotenv import load_dotenv
# from app.routes import auth, profiles, social_links
from app.db.session import engine
# from app.models import user, profile, social_link
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routes import auth
from app.routes import profiles
from app.models import user
from app.models import profile
from app.models import notification
from app.routes import store


load_dotenv()



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables - not convenient in production as this lacks version control for schema changes, Doesn't handle migrations/rollbacks
    user.Base.metadata.create_all(bind=engine)
    profile.Base.metadata.create_all(bind=engine)
    notification.Base.metadata.create_all(bind=engine)

    
    yield
    # social_link.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Profile Fusion API", version="0.1.0",lifespan=lifespan)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(profiles.router, prefix="/profiles", tags=["Profiles"])
app.include_router(store.router, prefix="/stores", tags=["Stores"])

