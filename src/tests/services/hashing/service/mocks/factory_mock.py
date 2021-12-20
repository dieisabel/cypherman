__all__ = ['HashingAlgorithmFactoryMock']

from typing import List, Optional

from entities.hashing_algorithms import IHashingAlgorithm
from services.hashing.factories import IHashingAlgorithmFactory
from tests.services.hashing.service.mocks import (
    MD5HashingAlgorithmMock,
    SHA1HashingAlgorithmMock,
)


class HashingAlgorithmFactoryMock(IHashingAlgorithmFactory):
    def create_algorithm(self, algorithm_name: str) -> Optional[IHashingAlgorithm]:
        if algorithm_name == 'md5':
            return MD5HashingAlgorithmMock()
        if algorithm_name == 'sha1':
            return SHA1HashingAlgorithmMock()
        return None

    def get_available_algorithms(self) -> List[str]:
        return ['md5', 'sha1']
