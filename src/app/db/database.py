__all__ = [
    'DatabaseSession',
    'AlchemyMetadata',
]

from functools import lru_cache

from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.orm import sessionmaker, Session

from config import get_settings, Settings


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
    settings: Settings = get_settings()
    return create_engine(
        url=settings.SQLALCHEMY_DATABASE_URL,
        echo=settings.SQLALCHEMY_ECHO,
    )
