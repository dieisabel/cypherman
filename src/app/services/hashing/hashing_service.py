__all__ = ['HashingService']

from typing import List, Optional

from fastapi import Depends

from services.hashing import IHashingService
from services.hashing.factories import (
    HashingAlgorithmFactory,
    IHashingAlgorithmFactory,
)
from entities.hashing_algorithms import IHashingAlgorithm
from schemas import HashesDTO


class HashingService(IHashingService):
    _factory: IHashingAlgorithmFactory

    def __init__(
        self, factory: IHashingAlgorithmFactory = Depends(HashingAlgorithmFactory)
    ) -> None:
        self._factory = factory

    def hash_user_data(self, data: str, algorithm_name: str) -> Optional[HashesDTO]:
        algorithm: Optional[IHashingAlgorithm] = self._factory.create_algorithm(algorithm_name)
        if not algorithm:
            return None
        return self._generate_dto(algorithm, algorithm.hash(data))

    def get_available_algorithms(self) -> List[str]:
        return self._factory.get_available_algorithms()

    # TODO: Maybe we should create separate class that will create dtos?
    def _generate_dto(self, algorithm: IHashingAlgorithm, checksum: str) -> HashesDTO:
        return HashesDTO(
            algorithm=algorithm.name,
            bits=algorithm.bits,
            checksum=checksum,
            is_secure=algorithm.is_secure
        )
