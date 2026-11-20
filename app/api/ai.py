from fastapi import APIRouter, Depends

from app.config.dependencies import get_ai_service
from app.schemas.ai import Ai_Schema
from app.services.ai import Ai_Service


router = APIRouter(prefix='/ai')

@router.post('/ask')
async def ask_llm(payload: Ai_Schema, ai_service: Ai_Service = Depends(get_ai_service)):
    return await ai_service.ask_llm(payload.text)