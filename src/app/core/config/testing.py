"""Module for testing configuration"""

__all__ = ['TestingConfig']

import os

from core.config.base import BaseConfig


class TestingConfig(BaseConfig):
    """Settings for testing environment"""

    SQLALCHEMY_DATABASE_URL: str = os.environ.get('SQLALCHEMY_DATABASE_URL')
    SQLALCHEMY_ECHO: bool = False
