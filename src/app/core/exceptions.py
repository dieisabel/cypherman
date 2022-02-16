"""Module for application exceptions"""

__all__ = [
    'ImproperlyConfigured'
]


class ImproperlyConfigured(Exception):
    """Indicates that there are something wrong with application configuration"""
