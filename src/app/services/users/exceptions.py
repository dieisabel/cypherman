"""Module for user service exceptions"""

__all__ = [
    'UserNotFoundException',
    'UserIsExistsException',
]


class UserNotFoundException(Exception):
    """Indicates that user not found

    Args:
        message: Detailed message
    """

    def __init__(self, message: str) -> None:
        self.message = message


class UserIsExistsException(Exception):
    """Indicates that user is already exists in database

    Args:
        message: Detailed message
    """

    def __init__(self, message: str) -> None:
        self.message = message
