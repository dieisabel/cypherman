"""Module for hashing service implementation"""

__all__ = ['HashingService']

from typing import List
from typing import Optional

from fastapi import Depends

from services.hashing import IHashingService
from services.hashing.factories import HashingAlgorithmFactory
from services.hashing.factories import IHashingAlgorithmFactory
from entities.hashing_algorithms import IHashingAlgorithm
from dtos import HashesDTO


class HashingService(IHashingService):
    """Hashing service implementation

    Args:
        factory: Factory for creating hashing algorithms
    """

    def __init__(self, factory: IHashingAlgorithmFactory = Depends(HashingAlgorithmFactory)) -> None:
        self._factory = factory

    def hash_user_data(self, request: HashesDTO.Request) -> Optional[HashesDTO.Response]:
        """Hash user data

        Args:
            request: HashesRequest object with data

        Returns:
            HashesResponse with all needed data
        """

        algorithm: Optional[IHashingAlgorithm] = self._factory.create_algorithm(request.algorithm)
        if not algorithm:
            return None
        return self._generate_response(algorithm, algorithm.hash(request.data))

    def get_available_algorithms(self) -> List[str]:
        """Get available hashing algorithms

        Returns:
            A list with supported hashing algorihtms
        """

        return self._factory.get_available_algorithms()

    @staticmethod
    def _generate_response(algorithm: IHashingAlgorithm, checksum: str) -> HashesDTO.Response:
        return HashesDTO.Response(
            algorithm=algorithm.name,
            bits=algorithm.bits,
            checksum=checksum,
            is_secure=algorithm.is_secure
        )
