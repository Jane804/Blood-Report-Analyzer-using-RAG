from pydantic import BaseModel
from fastapi import APIRouter

from app.rag.retriever import retrieve_context
from app.services.summary_service import answer_question

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    context = retrieve_context(
        request.question
    )

    answer = answer_question(
        request.question,
        context
    )

    return {
        "question": request.question,
        "answer": answer,
        "context": context
    }