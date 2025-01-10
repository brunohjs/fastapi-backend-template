import os
from functools import lru_cache

from dotenv import load_dotenv

from src.config.environment import Environment
from src.config.settings.base import BaseSettings
from src.config.settings.development import DevSettings
from src.config.settings.production import ProdSettings
from src.config.settings.qa import QASettings


@lru_cache()
def get_settings() -> BaseSettings:
    load_dotenv(".env")
    environment = os.environ.get("ENV")
    if environment == Environment.DEVELOPMENT:
        return DevSettings()
    elif environment == Environment.QA:
        return QASettings()
    elif environment == Environment.PRODUCTION:
        return ProdSettings()
    else:
        raise ValueError()


settings: BaseSettings = get_settings()
