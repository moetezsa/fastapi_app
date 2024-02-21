from pydantic.v1 import BaseSettings


class AppConfig(BaseSettings):
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
