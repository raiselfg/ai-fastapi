from fastapi import APIRouter
from app.api.ai import router as ai_router

router = APIRouter(prefix='/api/v1')

router.include_router(ai_router)