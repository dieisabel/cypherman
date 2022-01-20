"""Module for User Repository"""

__all__ = ['UserRepository']

from typing import Optional

from sqlalchemy.orm import Session

from repositories.user.iuser_repository import IUserRepository
from entities.users import User


class UserRepository(IUserRepository):
    """User repository

    :param session: Session object to work with database
    """

    def __init__(self, session: Session) -> None:
        self._session = session

    def find_by_id(self, identifier: int) -> Optional[User]:
        """Find User by its identifier

        :param identifier: Identifier
        :return: User entity if User with this identifier exists in database
        """
        return self._session.query(User).get(identifier)

    def add(self, entity: User) -> None:
        """Add User object to a database table

        :param entity: User entity
        :return: None
        """
        self._session.add(entity)

    def remove(self, entity: User) -> None:
        """Remove specified User from database table

        :param entity:
        :return: None
        """
        self._session.delete(entity)
