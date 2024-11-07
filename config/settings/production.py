from config.settings.base import BaseSettings
from config.environment import Environment


class ProdSettings(BaseSettings):
    DESCRIPTION: str | None = "Production Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.PRODUCTION
