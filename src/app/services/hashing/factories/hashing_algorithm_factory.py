__all__ = ['HashingAlgorithmFactory']

from typing import Optional, Dict, List

from entities.hashing_algorithms import (
    IHashingAlgorithm,
    MD5HashingAlgorithm,
    SHA1HashingAlgorithm,
    SHA256HashingAlgorithm,
)
from services.hashing.factories import IHashingAlgorithmFactory


class HashingAlgorithmFactory(IHashingAlgorithmFactory):
    def __init__(self) -> None:
        # TODO: Maybe store registry in settings?
        self._registry: Dict[str, IHashingAlgorithm] = {    # type: ignore
            'md5': MD5HashingAlgorithm,
            'sha1': SHA1HashingAlgorithm,
            'sha256': SHA256HashingAlgorithm,
        }

    def create_algorithm(self, algorithm_name: str) -> Optional[IHashingAlgorithm]:
        processed_name: str = self._process_name(algorithm_name)
        if processed_name not in self.get_available_algorithms():
            return None
        algorithm_class: IHashingAlgorithm = self._registry.get(processed_name)
        return algorithm_class()

    def get_available_algorithms(self) -> List[str]:
        return list(self._registry.keys())

    # TODO: Why factory also processes strings?
    def _process_name(self, name: str) -> str:
        return name.strip().lower()
