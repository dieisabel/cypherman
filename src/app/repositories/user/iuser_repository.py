"""Module for User Repository interface"""

__all__ = ['IUserRepository']

from abc import ABC
from abc import abstractmethod
from typing import Optional

from entities.users import User


class IUserRepository(ABC):
    """User Repository Interface"""

    @abstractmethod
    def find_by_id(self, identifier: int) -> Optional[User]:
        """Find User by its identifier

        :param identifier: Identifier
        :return: User entity if User with this identifier exists in database
        """
        raise NotImplementedError

    @abstractmethod
    def add(self, entity: User) -> None:
        """Add User object to a database table

        :param entity: User entity
        :return: None
        """
        raise NotImplementedError

    @abstractmethod
    def remove(self, entity: User) -> None:
        """Remove specified User from database table

        :param entity:
        :return: None
        """
        raise NotImplementedError
