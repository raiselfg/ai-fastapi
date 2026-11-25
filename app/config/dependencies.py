from fastapi import Depends
from openai import AsyncOpenAI
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.ai import get_ai_client
from app.config.db import get_db
from app.services.ai import AiService
from app.services.conversation import ConversationService


def get_ai_service(ai_client: AsyncOpenAI = Depends(get_ai_client)) -> AiService:
    return AiService(ai_client)

def get_conversations_service(db: AsyncSession = Depends(get_db)) -> ConversationService:
    return ConversationService(db)