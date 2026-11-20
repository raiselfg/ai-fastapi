from functools import lru_cache
from openai import AsyncOpenAI

from app.config.settings import get_settings

@lru_cache
def get_ai_client() -> AsyncOpenAI:
    settings = get_settings()

    return AsyncOpenAI(
        api_key=settings.ai_api_token,
        base_url=settings.ai_url,
        timeout=20.0,
    )