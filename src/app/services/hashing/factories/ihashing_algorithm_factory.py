__all__ = ['IHashingAlgorithmFactory']

from abc import ABC, abstractmethod
from typing import Optional, List

from entities.hashing_algorithms import IHashingAlgorithm


class IHashingAlgorithmFactory(ABC):

    @abstractmethod
    def create_algorithm(self, algorithm_name: str) -> Optional[IHashingAlgorithm]:
        raise NotImplementedError

    @abstractmethod
    def get_available_algorithms(self) -> List[str]:
        raise NotImplementedError
