__all__ = ['TestingConfig']

from core.config.base import BaseConfig


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URL: str = 'sqlite:///:memory:'
    SQLALCHEMY_ECHO: bool = False
