"""Module for database initialization function"""

__all__ = ['initialize_database']

from core.db.mappers import start_mappers
from core.db.dependencies import AlchemyMetadata


def initialize_database() -> None:
    """Initialize database

    Creates all tables and maps entities to its appropriate tables. Intended to use only once at application creating,
    overwise there will be an error, which indicates that entities already have defined mappers.

    :return: None
    """
    AlchemyMetadata().create_all()
    start_mappers()
