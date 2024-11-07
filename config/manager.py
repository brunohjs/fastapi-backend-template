from functools import lru_cache

import decouple

from config.environment import Environment
from config.settings.base import BaseSettings
from config.settings.development import DevSettings
from config.settings.qa import QASettings
from config.settings.production import ProdSettings


@lru_cache()
def get_settings() -> BaseSettings:
    environment = decouple.config("ENVIRONMENT", "DEV")
    if environment == Environment.DEVELOPMENT.value:
        return DevSettings()
    elif environment == Environment.QA.value:
        return QASettings()
    return ProdSettings()


settings: BaseSettings = get_settings()
