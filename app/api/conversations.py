from fastapi import APIRouter, Depends

from app.config.dependencies import get_conversations_service
from app.schemas.conversations import ConversationRequest, ConversationResponse
from app.services.conversation import ConversationService


router = APIRouter(prefix="/conversation")

@router.post("/", response_model=ConversationResponse)
async def create_conversation(payload: ConversationRequest, cv_service: ConversationService = Depends(get_conversations_service)):
    return await cv_service.create_conversation(payload.title)