import enum


class Environment(str, enum.Enum):
    DEVELOPMENT: str = "DEV"
    QA: str = "QA"
    PRODUCTION: str = "PROD"
