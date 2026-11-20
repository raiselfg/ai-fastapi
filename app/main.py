from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.config.ai import ai_client
from app.api.router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.ai_client = ai_client
    yield
    await app.state.ai_client.close()

app = FastAPI(lifespan=lifespan)

app.include_router(router)