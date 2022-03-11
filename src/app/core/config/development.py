"""Module for development configuration"""

__all__ = ['DevelopmentConfig']

import os

from core.config.base import BaseConfig


class DevelopmentConfig(BaseConfig):
    """Settings for development environment"""

    SQLALCHEMY_DATABASE_URL: str = os.environ['SQLALCHEMY_DATABASE_URL']
    SQLALCHEMY_ECHO: bool = True
