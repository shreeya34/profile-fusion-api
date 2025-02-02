from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_profiles():
    return {"message": "List of profiles"}