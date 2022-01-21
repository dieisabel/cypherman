"""Module for User Repository interface"""

__all__ = ['IUserRepository']

from abc import ABC
from abc import abstractmethod
from typing import Optional
from typing import List

from entities.users import User


class IUserRepository(ABC):
    """User Repository Interface"""

    @abstractmethod
    def find_user_by_id(self, identifier: int) -> Optional[User]:
        """Find user by its identifier

        :param identifier: Identifier
        :return: User entity if User with this identifier exists in database
        """
        raise NotImplementedError

    @abstractmethod
    def find_all_users(self) -> List[User]:
        """Find all users

        :return: A list with users, may be empty if there are no users in database
        """
        raise NotImplementedError

    @abstractmethod
    def add_user(self, entity: User) -> None:
        """Add user object to a database table

        :param entity: User entity
        :return: Created User object
        """
        raise NotImplementedError

    @abstractmethod
    def remove_user(self, entity: User) -> None:
        """Remove specified user from database table

        :param entity: User to delete
        :return: None
        """
        raise NotImplementedError
