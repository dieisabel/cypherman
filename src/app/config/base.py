__all__ = [
    'Config',
    'BaseConfig',
]

from pydantic import BaseSettings


class Config(BaseSettings):
    pass


class BaseConfig(Config):
    APPLICATION_NAME: str = 'Cypherman'
    APPLICATION_DESCRIPTION: str = 'Secure your data with Cypherman!'
    VERSION: str = '0.0.0'
