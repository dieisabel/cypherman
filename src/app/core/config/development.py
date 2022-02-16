"""Module for development configuration"""

__all__ = ['DevelopmentConfig']

from core.config.base import BaseConfig


class DevelopmentConfig(BaseConfig):
    """Settings for development environment"""

    SQLALCHEMY_DATABASE_URL: str
    SQLALCHEMY_ECHO: bool = True

    class Config:
        env_file = '.env.development'
