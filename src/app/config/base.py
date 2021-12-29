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

    # TODO: This settings also applied to tests, so we need to make separate Dev and Testing settings
    SQLALCHEMY_DATABASE_URL: str = 'sqlite:///./db.sqlite3'
    SQLALCHEMY_ECHO: bool = False

    class Config:
        env_file = '.env'
