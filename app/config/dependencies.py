from fastapi import Depends
from openai import AsyncOpenAI
from app.config.ai import get_ai_client
from app.services.ai import AiService

def get_ai_service(ai_client: AsyncOpenAI = Depends(get_ai_client)) -> AiService:
    return AiService(ai_client)