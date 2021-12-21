__all__ = ['HashingService']

from typing import List, Optional

from fastapi import Depends

from services.hashing import IHashingService
from services.hashing.factories import (
    HashingAlgorithmFactory,
    IHashingAlgorithmFactory,
)
from entities.hashing_algorithms import IHashingAlgorithm
from dtos import HashesDTO


class HashingService(IHashingService):
    _factory: IHashingAlgorithmFactory

    def __init__(self, factory: IHashingAlgorithmFactory = Depends(HashingAlgorithmFactory)) -> None:
        self._factory = factory

    def hash_user_data(self, request: HashesDTO.Request) -> Optional[HashesDTO.Response]:
        algorithm: Optional[IHashingAlgorithm] = self._factory.create_algorithm(request.algorithm)
        if not algorithm:
            return None
        return self._generate_response(algorithm, algorithm.hash(request.data))

    def get_available_algorithms(self) -> List[str]:
        return self._factory.get_available_algorithms()

    # TODO: Maybe we should create separate class that will create response?
    @staticmethod
    def _generate_response(algorithm: IHashingAlgorithm, checksum: str) -> HashesDTO.Response:
        return HashesDTO.Response(
            algorithm=algorithm.name,
            bits=algorithm.bits,
            checksum=checksum,
            is_secure=algorithm.is_secure
        )
