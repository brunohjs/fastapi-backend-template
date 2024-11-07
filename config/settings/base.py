import decouple
import pydantic_settings


class BaseSettings(pydantic_settings.BaseSettings):
    APP_NAME: str = decouple.config("APP_NAME", "Minha API FastAPI")
    API_VERSION: str = decouple.config("API_VERSION", "v1")
    DEBUG: bool = decouple.config("DEBUG", True)
    DESCRIPTION: str = decouple.config("DESCRIPTION", "")
    ENVIRONMENT: str = decouple.config("ENVIRONMENT", "DEV")

    API_HOST: str = decouple.config("API_HOST", "localhost")
    API_PORT: int = decouple.config("API_PORT", "8000")
    API_PREFIX: str = decouple.config("API_PREFIX", "")
    DOCS_URL: str = decouple.config("DOCS_URL", "/docs")
    REDOC_URL: str = decouple.config("REDOC_URL", "/redoc")

    DATABASE_URL: str = decouple.config("DATABASE_URL", "sqlite:///./test.db")
    DATABASE_USERNAME: str = decouple.config("DATABASE_USERNAME", "")
    DATABASE_PASSWORD: str = decouple.config("DATABASE_PASSWORD", "")
    DATABASE_PORT: int = decouple.config("DATABASE_PORT", 8191)

    class Config:
        env_file = ".env"  # Define que as variáveis podem ser carregadas de um arquivo .env
