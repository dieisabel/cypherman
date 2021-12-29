__all__ = [
    'Settings',
    'get_settings',
]

from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    APPLICATION_NAME: str = 'Cypherman'
    APPLICATION_DESCRIPTION: str = 'Secure your data with Cypherman!'
    VERSION: str = '0.0.0'

    SQLALCHEMY_DATABASE_URL: str
    SQLALCHEMY_ECHO: bool

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings() -> Settings:
    return Settings()
