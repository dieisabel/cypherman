"""Module for start_mappers function that starts all entity to table mappers

start_mappers() function intended to use once and only while main application creation. If call more than once where
will be an error that tells that tables, which mappers must create and map entity to them, already exist.
"""

__all__ = ['start_mappers']


def start_mappers() -> None:
    """Start all mappers

    :return: None
    """
