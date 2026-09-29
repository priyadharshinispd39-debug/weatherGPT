from fastapi import APIRouter
from pydantic import BaseModel
from ..services.advisory_engine import answer_question
router = APIRouter(tags=["Chat"])
class ChatRequest(BaseModel):
    question: str
    city: str = "Chennai"
    role: str = "Citizen"
    language: str = "English"
@router.post("/chat")
def chat(req: ChatRequest):
    return answer_question(req.question, req.city, req.role, req.language)
