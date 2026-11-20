from openai import AsyncClient

from app.config.settings import settings

ai_client = AsyncClient(api_key=settings.ai_api_token, base_url=settings.ai_url)