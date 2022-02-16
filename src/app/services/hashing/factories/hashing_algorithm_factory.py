"""Module for hashing algorithm factory implementation"""

__all__ = ['HashingAlgorithmFactory']

from typing import Optional
from typing import Dict
from typing import List
from typing import Type

from entities.hashing_algorithms import IHashingAlgorithm
from entities.hashing_algorithms import MD5HashingAlgorithm
from entities.hashing_algorithms import SHA1HashingAlgorithm
from entities.hashing_algorithms import SHA256HashingAlgorithm
from services.hashing.factories import IHashingAlgorithmFactory

HASHING_ALGORITHM_REGISTRY: Dict[str, Type[IHashingAlgorithm]] = {
    'md5': MD5HashingAlgorithm,
    'sha1': SHA1HashingAlgorithm,
    'sha256': SHA256HashingAlgorithm,
}


class HashingAlgorithmFactory(IHashingAlgorithmFactory):
    """Hashing algorithm factory implementation"""

    def __init__(self) -> None:
        self._registry = HASHING_ALGORITHM_REGISTRY

    def create_algorithm(self, algorithm_name: str) -> Optional[IHashingAlgorithm]:
        """Create and return hashing algorith by name or return None

        Args:
            algorithm_name: Algorithm name

        Returns:
            Hashing algorithm or None if algorithm is not supported
        """

        processed_name: str = self._process_name(algorithm_name)
        if processed_name not in self.get_available_algorithms():
            return None
        algorithm_class: Type[IHashingAlgorithm] = self._registry[processed_name]
        return algorithm_class()

    def get_available_algorithms(self) -> List[str]:
        """Get a list of available algorithms

        Returns:
            A list with available algorithms
        """

        return list(self._registry.keys())

    @staticmethod
    def _process_name(name: str) -> str:
        return name.strip().lower()
