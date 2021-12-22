__all__ = ['HashingAlgorithmFactory']

from typing import Optional, Dict, List, Type

from entities.hashing_algorithms import (
    IHashingAlgorithm,
    MD5HashingAlgorithm,
    SHA1HashingAlgorithm,
    SHA256HashingAlgorithm,
)
from services.hashing.factories import IHashingAlgorithmFactory


class HashingAlgorithmFactory(IHashingAlgorithmFactory):
    _registry: Dict[str, Type[IHashingAlgorithm]]

    def __init__(self) -> None:
        # TODO: Maybe store registry in settings?
        self._registry: Dict[str, Type[IHashingAlgorithm]] = {
            'md5': MD5HashingAlgorithm,
            'sha1': SHA1HashingAlgorithm,
            'sha256': SHA256HashingAlgorithm,
        }

    def create_algorithm(self, algorithm_name: str) -> Optional[IHashingAlgorithm]:
        """Create and return hashing algorith by name or return None

        :param algorithm_name: Algorithm name, no matter what case
        :return: Hashing algorithm or None if algorithm is not supported
        """

        processed_name: str = self._process_name(algorithm_name)
        if processed_name not in self.get_available_algorithms():
            return None
        algorithm_class: Type[IHashingAlgorithm] = self._registry.get(processed_name)
        return algorithm_class()

    def get_available_algorithms(self) -> List[str]:
        """Get a list of available algorithms

        :return: A list which contains available algorithms
        """

        return list(self._registry.keys())

    # TODO: Why factory also processes strings?
    def _process_name(self, name: str) -> str:
        return name.strip().lower()
