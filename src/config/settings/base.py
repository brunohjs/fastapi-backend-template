import os

import pydantic_settings


class BaseSettings(pydantic_settings.BaseSettings):
    APP_NAME: str = os.environ.get("APP_NAME", "Minha API FastAPI")
    API_VERSION: str = os.environ.get("API_VERSION", "v1")
    DEBUG: bool = os.environ.get("DEBUG", True)
    DESCRIPTION: str = os.environ.get("DESCRIPTION", "")
    ENVIRONMENT: str = os.environ.get("ENVIRONMENT", "DEV")

    API_HOST: str = os.environ.get("API_HOST", "localhost")
    API_PORT: int = os.environ.get("API_PORT", "8000")
    API_PREFIX: str = os.environ.get("API_PREFIX", "")
    DOCS_URL: str = os.environ.get("DOCS_URL", "/docs")
    REDOC_URL: str = os.environ.get("REDOC_URL", "/redoc")

    DATABASE_URL: str = os.environ.get("DATABASE_URL", "sqlite:///./test.db")
    DATABASE_USERNAME: str = os.environ.get("DATABASE_USERNAME", "")
    DATABASE_PASSWORD: str = os.environ.get("DATABASE_PASSWORD", "")
    DATABASE_PORT: int = os.environ.get("DATABASE_PORT", 8191)

    class Config:
        env_file = ".env"  # Define que as variáveis podem ser carregadas de um arquivo .env
