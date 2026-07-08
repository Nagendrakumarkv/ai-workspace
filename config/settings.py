from functools import lru_cache

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    """
    Application configuration.
    """

    gemini_api_key: str = Field(alias="GEMINI_API_KEY")

    model_name: str = Field(
        default="gemini-2.5-flash",
        alias="MODEL_NAME",
    )

    app_name: str = Field(
        default="AI Workspace",
        alias="APP_NAME",
    )

    debug: bool = Field(
        default=False,
        alias="DEBUG",
    )

    model_config = SettingsConfigDict(
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.
    """
    return Settings()