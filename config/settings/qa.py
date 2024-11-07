from config.settings.base import BaseSettings
from config.environment import Environment


class QASettings(BaseSettings):
    DESCRIPTION: str | None = "Test Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.QA
