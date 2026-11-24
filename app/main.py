from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import router
from app.config.ai import get_ai_client
from app.exceptions.ai import AiTimeoutError
from app.exceptions.handlers import ai_timeout_handler


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.ai_client = get_ai_client()
    yield
    await app.state.ai_client.close()


app = FastAPI(lifespan=lifespan)

app.include_router(router)

app.add_exception_handler(
    AiTimeoutError,
    ai_timeout_handler
)