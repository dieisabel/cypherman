"""Module for testing configuration"""

__all__ = ['TestingConfig']

from core.config.base import BaseConfig


class TestingConfig(BaseConfig):
    """Settings for testing environment"""

    SQLALCHEMY_DATABASE_URL: str = 'sqlite:///:memory:'
    SQLALCHEMY_ECHO: bool = False
