from fastapi import FastAPI

from app.lifespan import lifespan
from app.api.router import router
from app.exceptions.ai import AiTimeoutError
from app.exceptions.handlers import ai_timeout_handler


app = FastAPI(lifespan=lifespan)

app.include_router(router)

app.add_exception_handler(
    AiTimeoutError,
    ai_timeout_handler
)