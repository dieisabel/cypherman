"""Module for users data transfer objects and its mappers"""

__all__ = [
    'UsersRequest',
    'UsersResponse',
    'map_request_to_user',
    'map_user_to_response',
    'map_users_to_list_of_responses',
]

from dataclasses import dataclass
from typing import List
from typing import Optional

from entities.users import User


@dataclass
class UsersRequest:
    """Users request

    Object for transfering data from user controllers to a UserService.
    To map UsersRequest to a User entity use map_request_to_user function.

    Args:
        user_id: User identifier
        username: Username
        email: Email
    """

    user_id: int
    username: str
    email: Optional[str] = None


@dataclass
class UsersResponse:
    """Users response

    Object for transfering data from UserService to a users controllers.
    To map User entity to UsersResponse use map_user_to_response.

    Args:
        user_id: User identifier
        username: Username
        email: Email
    """

    user_id: int
    username: str
    email: Optional[str] = None


def map_request_to_user(request: UsersRequest) -> User:
    """Map users request to user entity

    Args:
        request: Users request

    Returns:
        User entity
    """

    return User(
        user_id=request.user_id,
        username=request.username,
        email=request.email
    )


def map_user_to_response(user: User) -> UsersResponse:
    """Map an user entity to a users response

    Args:
        user: User entity

    Returns:
        UsersResponse with user data
    """

    return UsersResponse(
        user_id=user.user_id,
        username=user.username,
        email=user.email,
    )


def map_users_to_list_of_responses(users: List[User]) -> List[UsersResponse]:
    """Map a list of users to a list of users responses

    Args:
        users: A list of user entities

    Returns:
        A list of users responses
    """

    return list(map(map_user_to_response, users))
