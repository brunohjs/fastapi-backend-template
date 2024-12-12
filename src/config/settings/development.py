from src.config.environment import Environment
from src.config.settings.base import BaseSettings


class DevSettings(BaseSettings):
    DESCRIPTION: str | None = "Development Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.DEVELOPMENT
