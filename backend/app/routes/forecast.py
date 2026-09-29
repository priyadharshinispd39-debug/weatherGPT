from fastapi import APIRouter
router = APIRouter(tags=["Forecast"])
@router.get("/forecast")
def forecast(city: str = "Chennai"):
    return {"city": city, "forecast": []}
