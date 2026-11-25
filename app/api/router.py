from fastapi import APIRouter

from app.api.ai import router as ai_router
from app.api.conversations import router as cv_router

router = APIRouter(prefix="/api/v1")

router.include_router(ai_router)
router.include_router(cv_router)
