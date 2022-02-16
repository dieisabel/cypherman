"""Module for user service implementation"""

__all__ = ['UserService']

from typing import List
from typing import Optional

from sqlalchemy.orm import Session

from services.users.iuser_service import IUserService
from entities.users import User
from dtos.users import UsersRequest
from dtos.users import UsersResponse
from dtos.users import map_request_to_user
from dtos.users import map_user_to_response
from dtos.users import map_users_to_list_of_responses
from repositories.user import IUserRepository
from repositories.user import UserRepository
from core.db import DatabaseSession
from services.users.exceptions import UserNotFoundException
from services.users.exceptions import UserIsExistsException


class UserService(IUserService):
    """User Service Implementation"""

    def __init__(self) -> None:
        self._session: Session = DatabaseSession()
        self._repository: IUserRepository = UserRepository(self._session)

    def find_all_users(self) -> List[UsersResponse]:
        """Find all users

        Returns:
            A list with UsersResponse objects, which contain user data
        """

        users: List[User] = self._repository.find_all_users()
        return map_users_to_list_of_responses(users)

    def find_user_by_id(self, user_id: int) -> UsersResponse:
        """Find user by user_id

        Args:
            user_id: User identifier

        Returns:
            UsersResponse object with user data

        Raises:
            UserNotFoundException: If user with specified user_id is not found
        """

        user: Optional[User] = self._repository.find_user_by_id(user_id)
        if not user:
            raise UserNotFoundException(f'User with user_id = {user_id} not found')
        return map_user_to_response(user)

    def add_user(self, request: UsersRequest) -> UsersResponse:
        """Add new user

        Args:
            request: UsersRequest with user data

        Returns:
            Added user

        Raises:
            UserIsExistsException: If user is already exists
        """

        if self._repository.find_user_by_id(request.user_id):
            raise UserIsExistsException(f'User with user_id = {request.user_id} is already exists')
        new_user: User = map_request_to_user(request)
        self._repository.add_user(new_user)
        return map_user_to_response(new_user)

    def remove_user(self, user_id: int) -> None:
        """Remove user

        Args:
            user_id: User identifier

        Raises:
            UserNotFoundException: If user with specified identifier is not found
        """

        user: Optional[User] = self._repository.find_user_by_id(user_id)
        if not user:
            raise UserNotFoundException(f'User with user_id = {user_id} not found')
        self._repository.remove_user(user)
        return None

    def commit(self) -> None:
        """Commit changes

        Needed to be called after operations
        """

        self._session.commit()
