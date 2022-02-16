"""Module for User entity"""

__all__ = ['User']

from typing import Optional


class User:
    """User entity

    Args:
        user_id: User unique identifier
        username: Username
        email: Email
    """

    def __init__(self, user_id: int, username: str, email: Optional[str] = None) -> None:
        self.user_id = user_id
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return f'User(user_id={self.user_id}, username={self.username}, email={self.email})'
