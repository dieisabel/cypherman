"""Module for User entity"""

__all__ = ['User']

from typing import Optional


class User:
    """User entity

    :param user_id: User unique identifier
    :param username: Username
    :param email: Email
    """

    def __init__(self, user_id: int, username: str, email: Optional[str]) -> None:
        self.user_id = user_id
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return f'User(user_id={self.user_id}, username={self.username}, email={self.email})'