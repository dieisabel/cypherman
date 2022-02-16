"""Module for start_mappers function that starts all entity to table mappers"""

__all__ = ['start_mappers']

from entities.users import mapper as user_mapper


def start_mappers() -> None:
    """Start all mappers

    Warning:
        Function intended to use once and only while main application creation. If call more than once where
        will be an error that tells that tables, which mappers must create and map entity to them, already exist.
    """

    user_mapper.start_mapper()
