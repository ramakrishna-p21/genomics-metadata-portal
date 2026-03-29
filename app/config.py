from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    app_env: str = Field(default="local", alias="APP_ENV")

    postgres_db: str = Field(default="genomics_portal", alias="POSTGRES_DB")
    postgres_user: str = Field(default="genomics_user", alias="POSTGRES_USER")
    postgres_password: str = Field(default="genomics_pass", alias="POSTGRES_PASSWORD")
    postgres_host: str = Field(default="localhost", alias="POSTGRES_HOST")
    postgres_port: int = Field(default=5432, alias="POSTGRES_PORT")

    database_url: str = Field(
        default="postgresql+psycopg://genomics_user:genomics_pass@localhost:5432/genomics_portal",
        alias="DATABASE_URL",
    )

    streamlit_server_port: int = Field(default=8501, alias="STREAMLIT_SERVER_PORT")
    streamlit_server_headless: bool = Field(default=True, alias="STREAMLIT_SERVER_HEADLESS")

    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()