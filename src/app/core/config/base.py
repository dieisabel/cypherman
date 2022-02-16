"""Module for base configuration and config interface"""

__all__ = [
    'Config',
    'BaseConfig',
]

from pydantic import BaseSettings


class Config(BaseSettings):
    """Config interface"""


class BaseConfig(Config):
    """Base settings which are included in all other configuration"""

    APPLICATION_NAME: str = 'Cypherman'
    APPLICATION_DESCRIPTION: str = 'Secure your data with Cypherman!'
    VERSION: str = '0.0.0'
