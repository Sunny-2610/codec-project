import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "codec-chat")
    app_env: str = os.getenv("APP_ENV", "development")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./chat.db")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    secret_key: str = os.getenv("JWT_SECRET_KEY", "replace-me-with-a-secure-secret")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    refresh_token_expire_days: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))
    allowed_origins: list[str] = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",")
    rate_limit_per_minute: int = int(os.getenv("RATE_LIMIT_PER_MINUTE", "120"))


settings = Settings()
