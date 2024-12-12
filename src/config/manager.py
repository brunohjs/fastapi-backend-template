from functools import lru_cache

import decouple

from src.config.environment import Environment
from src.config.settings.base import BaseSettings
from src.config.settings.development import DevSettings
from src.config.settings.production import ProdSettings
from src.config.settings.qa import QASettings


@lru_cache()
def get_settings() -> BaseSettings:
    environment = decouple.config("ENVIRONMENT", "DEV")
    if environment == Environment.DEVELOPMENT.value:
        return DevSettings()
    elif environment == Environment.QA.value:
        return QASettings()
    return ProdSettings()


settings: BaseSettings = get_settings()
