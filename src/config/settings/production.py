from src.config.environment import Environment
from src.config.settings.base import BaseSettings


class ProdSettings(BaseSettings):
    DESCRIPTION: str | None = "Production Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.PRODUCTION
