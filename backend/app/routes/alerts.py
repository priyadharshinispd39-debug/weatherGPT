from fastapi import APIRouter
router = APIRouter(tags=["Alerts"])
@router.get("/alerts")
def alerts(city: str = "Chennai"):
    return {"city": city, "alerts": [], "message": "Official warning feed can be connected here."}
