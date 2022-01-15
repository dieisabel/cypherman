"""Module for users table"""

__all__ = ['users_table']

from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from core.db import AlchemyMetadata

metadata: MetaData = AlchemyMetadata()

users_table: Table = Table(
    'users',
    metadata,
    Column('user_id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(40), nullable=False),
    Column('email', String(40)),
)
