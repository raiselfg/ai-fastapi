from contextlib import asynccontextmanager

from app.config.ai import get_ai_client
from app.config.db import create_database

from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.ai_client = get_ai_client()
    database = create_database()
    app.state.engine = database.engine
    app.state.session_factory = database.session_factory
    try:
        yield
    finally:
        await app.state.ai_client.close()
        await app.state.engine.dispose()
