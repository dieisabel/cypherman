"""Module for database constants

To work with SQLAlchemy we need some constants. Some of them used for connecting to database, other for creating
sessions. Those constants not indented to use in a code outside of db package.

Usage of constants listed below:
* CONFIG - current application configuration. To see what and how a config is set see
  :func:`core.config.dependencies.get_config`
* ENGINE - object to connect to a database.
* SESSION_MAKER - factory to create a database sessions.
* METADATA - a registry, which will contain references to tables.
"""

__all__ = [
    'SESSION_MAKER',
    'METADATA',
]

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.orm import sessionmaker

from core.config import get_config
from core.config import Config

CONFIG: Config = get_config()
ENGINE: MockConnection = create_engine(
    url=CONFIG.SQLALCHEMY_DATABASE_URL,    # type: ignore
    echo=CONFIG.SQLALCHEMY_ECHO,           # type: ignore
)
SESSION_MAKER: sessionmaker = sessionmaker(bind=ENGINE)
METADATA: MetaData = MetaData()
