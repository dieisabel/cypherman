"""Module for user repository implementation"""

__all__ = ['UserRepository']

from typing import Optional
from typing import List

from sqlalchemy.orm import Session

from repositories.user.iuser_repository import IUserRepository
from entities.users import User


class UserRepository(IUserRepository):
    """User repository implementation

    Args:
        session: Session object to work with database
    """

    def __init__(self, session: Session) -> None:
        self._session = session

    def find_user_by_id(self, identifier: int) -> Optional[User]:
        """Find user by its identifier

        Args:
            identifier: User identifier

        Returns:
            User entity if User with identifier exists, otherwise None
        """

        return self._session.query(User).get(identifier)

    def find_all_users(self) -> List[User]:
        """Find all users

        Returns:
            A list with users, may be empty if there are no users
        """

        return self._session.query(User).all()

    def add_user(self, entity: User) -> None:
        """Add user object to a database table

        Args:
            entity: User entity
        """

        self._session.add(entity)

    def remove_user(self, entity: User) -> None:
        """Remove specified user from database table

        Args:
            entity: User that you want to remove
        """

        self._session.delete(entity)
