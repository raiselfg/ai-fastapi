from fastapi import APIRouter, Depends, status

from app.config.dependencies import get_ai_service
from app.schemas.ai import AiRequest, AiResponse
from app.services.ai import AiService

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/ask", response_model=AiResponse, status_code=status.HTTP_200_OK)
async def ask_llm(payload: AiRequest, ai_service: AiService = Depends(get_ai_service)):
    return await ai_service.ask_llm(payload.question, payload.temperature)
