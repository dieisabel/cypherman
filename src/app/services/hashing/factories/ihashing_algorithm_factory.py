"""Module for hashing algorithm factory interface"""

__all__ = ['IHashingAlgorithmFactory']

from abc import ABC
from abc import abstractmethod
from typing import Optional
from typing import List

from entities.hashing_algorithms import IHashingAlgorithm


class IHashingAlgorithmFactory(ABC):
    """Hashign algorithm factory interface"""

    @abstractmethod
    def create_algorithm(self, algorithm_name: str) -> Optional[IHashingAlgorithm]:
        """Create and return hashing algorith by name or return None

        Args:
            algorithm_name: Algorithm name

        Returns:
            Hashing algorithm or None if algorithm is not supported
        """

        raise NotImplementedError

    @abstractmethod
    def get_available_algorithms(self) -> List[str]:
        """Get a list of available algorithms

        Returns:
            A list with available algorithms
        """

        raise NotImplementedError
