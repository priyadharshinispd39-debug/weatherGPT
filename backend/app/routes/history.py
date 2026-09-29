from fastapi import APIRouter
router = APIRouter(tags=["History"])
@router.get("/history")
def history(city: str = "Chennai"):
    return {"city": city, "history": []}
