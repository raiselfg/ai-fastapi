from fastapi import Depends
from app.config.settings import Settings, get_settings
from app.services.ai import Ai_Service


def get_ai_service(settings: Settings = Depends(get_settings)) -> Ai_Service:
    return Ai_Service(settings)