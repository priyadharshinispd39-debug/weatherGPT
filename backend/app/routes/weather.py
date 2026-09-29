from fastapi import APIRouter
from ..services.weather_service import get_weather
router = APIRouter(tags=["Weather"])
@router.get("/weather")
def weather(city: str = "Chennai"):
    return get_weather(city)
