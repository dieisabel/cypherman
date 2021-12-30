__all__ = ['DevelopmentConfig']

from config.base import BaseConfig


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URL: str
    SQLALCHEMY_ECHO: bool = True

    class Config:
        env_file = '.env.development'
