from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env"),
        env_file_encoding="utf-8",
    )

    ai_api_token: str
    ai_base_url: str

    pg_user: str
    pg_password: str
    pg_db: str
    pg_port: int
    pg_host: str

@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
