from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter(tags=["Profile"])
class Profile(BaseModel):
    name: str = "WeatherGPT User"
    city: str = "Chennai"
    role: str = "Citizen"
    language: str = "English"
@router.post("/profile")
def save_profile(profile: Profile):
    return {"status": "saved", "profile": profile.model_dump()}
