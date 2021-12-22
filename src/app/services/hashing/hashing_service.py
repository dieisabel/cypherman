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
        """HashingService constructor

        :param factory: Hashing algorithm factory, which is used to work with hashing algorithms
        """

        self._factory = factory

    def hash_user_data(self, request: HashesDTO.Request) -> Optional[HashesDTO.Response]:
        """Hash user data

        :param request: A request object that contains data and algorithm to use
        :return: HashesDTO with all needed data: algorithm, bits, checksum and is_secure flag
        """

        algorithm: Optional[IHashingAlgorithm] = self._factory.create_algorithm(request.algorithm)
        if not algorithm:
            return None
        return self._generate_response(algorithm, algorithm.hash(request.data))

    def get_available_algorithms(self) -> List[str]:
        """Get available hashing algorithms

        :return: A list which contains supported hashing algorithms
        """

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
