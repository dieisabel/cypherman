"""Module for User Repository"""

__all__ = ['UserRepository']

from typing import Optional
from typing import List

from sqlalchemy.orm import Session

from repositories.user.iuser_repository import IUserRepository
from entities.users import User


class UserRepository(IUserRepository):
    """User repository

    :param session: Session object to work with database
    """

    def __init__(self, session: Session) -> None:
        self._session = session

    def find_user_by_id(self, identifier: int) -> Optional[User]:
        """Find user by its identifier

        :param identifier: Identifier
        :return: User entity if User with this identifier exists in database
        """
        return self._session.query(User).get(identifier)

    def find_all_users(self) -> List[User]:
        """Find all users

        :return: A list with users, may be empty if there are no users in database
        """
        return self._session.query(User).all()

    def add_user(self, entity: User) -> None:
        """Add user object to a database table

        :param entity: User entity
        :return: Created User object
        """
        self._session.add(entity)

    def remove_user(self, entity: User) -> None:
        """Remove specified user from database table

        :param entity: User to delete
        :return: None
        """
        self._session.delete(entity)
