__all__ = ['IHashingAlgorithmFactory']

from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Type

from entities.hashing_algorithms import IHashingAlgorithm


class IHashingAlgorithmFactory(ABC):
    _registry: Dict[str, Type[IHashingAlgorithm]]

    @abstractmethod
    def create_algorithm(self, algorithm_name: str) -> Optional[IHashingAlgorithm]:
        """Create and return hashing algorith by name or return None

        :param algorithm_name: Algorithm name, no matter what case
        :return: Hashing algorithm or None if algorithm is not supported
        """

        raise NotImplementedError

    @abstractmethod
    def get_available_algorithms(self) -> List[str]:
        """Get a list of available algorithms

        :return: A list which contains available algorithms
        """

        raise NotImplementedError
