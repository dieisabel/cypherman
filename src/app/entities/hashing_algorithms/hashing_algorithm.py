"""Module for hashing algorithm interface"""

__all__ = ['IHashingAlgorithm']

from abc import ABC, abstractmethod


class IHashingAlgorithm(ABC):
    """Hashing algorithm interface"""

    @abstractmethod
    def hash(self, data: str) -> str:
        """Hash data

        Args:
            data: Data to hash

        Returns:
            Checksum
        """

        raise NotImplementedError
