"""Module for user repository interface"""

__all__ = ['IUserRepository']

from abc import ABC
from abc import abstractmethod
from typing import Optional
from typing import List

from entities.users import User


class IUserRepository(ABC):
    """User repository interface"""

    @abstractmethod
    def find_user_by_id(self, identifier: int) -> Optional[User]:
        """Find user by its identifier

        Args:
            identifier: User identifier

        Returns:
            User entity if User with identifier exists, otherwise None
        """

        raise NotImplementedError

    @abstractmethod
    def find_all_users(self) -> List[User]:
        """Find all users

        Returns:
            A list with users, may be empty if there are no users
        """

        raise NotImplementedError

    @abstractmethod
    def add_user(self, entity: User) -> None:
        """Add user object to a database table

        Args:
            entity: User entity
        """

        raise NotImplementedError

    @abstractmethod
    def remove_user(self, entity: User) -> None:
        """Remove specified user from database table

        Args:
            entity: User that you want to remove
        """

        raise NotImplementedError
