from src.config.environment import Environment
from src.config.settings.base import BaseSettings


class QASettings(BaseSettings):
    DESCRIPTION: str | None = "Test Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.QA
