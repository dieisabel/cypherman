"""Module for user service interface"""

__all__ = ['IUserService']

from abc import ABC
from abc import abstractmethod
from typing import List

from dtos.users import UsersRequest
from dtos.users import UsersResponse


class IUserService(ABC):
    """User Service Interface"""

    @abstractmethod
    def find_all_users(self) -> List[UsersResponse]:
        """Find all users

        Returns:
            A list with UsersResponse objects, which contain user data
        """
        raise NotImplementedError

    @abstractmethod
    def find_user_by_id(self, user_id: int) -> UsersResponse:
        """Find user by user_id

        Args:
            user_id: User identifier

        Returns:
            UsersResponse object with user data

        Raises:
            UserNotFoundException: If user with specified user_id is not found
        """
        raise NotImplementedError

    @abstractmethod
    def add_user(self, request: UsersRequest) -> UsersResponse:
        """Add new user

        Args:
            request: UsersRequest with user data

        Returns:
            Added user

        Raises:
            UserIsExistsException: If user is already exists
        """
        raise NotImplementedError

    @abstractmethod
    def remove_user(self, user_id: int) -> None:
        """Remove user

        Args:
            user_id: User identifier

        Returns:
            None

        Raises:
            UserNotFoundException: If user with specified identifier is not found
        """
        raise NotImplementedError
