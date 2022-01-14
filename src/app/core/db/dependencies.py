"""Module contains database dependencies that you can use outside of database package"""

__all__ = [
    'DatabaseSession',
    'AlchemyMetadata',
]

from sqlalchemy import MetaData
from sqlalchemy.orm import Session

from core.db.constants import SESSION_MAKER
from core.db.constants import METADATA


def DatabaseSession() -> Session:
    """Get database session

    :return: New database session

    Example:
    >>> session: Session = DatabaseSession()
    >>> session.execute('SELECT * FROM users;')
    >>> # Or add some instances using session.add(instance), then commit changes using session.commit()
    """
    return SESSION_MAKER()


def AlchemyMetadata() -> MetaData:
    """Get SQLAlchemy MetaData object

    :return: MetaData object
    """
    return METADATA
