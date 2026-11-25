from fastapi import APIRouter, Depends, status

from app.config.dependencies import get_conversations_service
from app.schemas.conversations import ConversationRequest, ConversationResponse
from app.services.conversation import ConversationService


router = APIRouter(prefix="/conversation", tags=["conversation"])

@router.post("", response_model=ConversationResponse, status_code=status.HTTP_201_CREATED)
async def create_conversation(payload: ConversationRequest, cv_service: ConversationService = Depends(get_conversations_service)):
    return await cv_service.create_conversation(payload.title)