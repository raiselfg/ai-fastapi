from collections.abc import AsyncIterator
from functools import lru_cache
from typing import NamedTuple

from fastapi import Request
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config.settings import get_settings


class Database(NamedTuple):
    engine: AsyncEngine
    session_factory: async_sessionmaker[AsyncSession]

def get_database_url() -> URL:
    settings = get_settings()

    return URL.create(
        "postgresql+asyncpg",
        username=settings.pg_user,
        password=settings.pg_password,
        host=settings.pg_host,
        port=settings.pg_port,
        database=settings.pg_db,
    )

@lru_cache
def create_database() -> Database:
    engine = create_async_engine(
        get_database_url(), pool_pre_ping=True, hide_parameters=True
    )
    return Database(engine, async_sessionmaker(engine, expire_on_commit=False))


async def get_db(request: Request) -> AsyncIterator[AsyncSession]:
    async with request.app.state.session_factory() as session:
        yield session
