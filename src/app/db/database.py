__all__ = [
    'DatabaseSession',
    'AlchemyMetadata',
]

from functools import lru_cache

from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.orm import sessionmaker, Session

from core.config import get_config, Config


def DatabaseSession() -> Session:
    session_maker: sessionmaker = _get_session_maker()
    return session_maker()


@lru_cache
def AlchemyMetadata() -> MetaData:
    return MetaData()


@lru_cache
def _get_session_maker() -> sessionmaker:
    return sessionmaker(bind=_get_engine())


@lru_cache
def _get_engine() -> MockConnection:
    config: Config = get_config()
    return create_engine(
        url=config.SQLALCHEMY_DATABASE_URL,    # type: ignore
        echo=config.SQLALCHEMY_ECHO,           # type: ignore
    )
