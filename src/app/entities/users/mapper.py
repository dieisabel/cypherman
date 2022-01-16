"""Module for mapper that maps User entity to its users table"""

__all__ = ['start_mapper']

from sqlalchemy.orm import mapper
from sqlalchemy.orm import Mapper

from entities.users import User
from entities.users.table import users_table


def start_mapper() -> Mapper:
    """Start mapper that maps User entity to its users table

    :return: Mapper object
    """
    return mapper(User, users_table)
