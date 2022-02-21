"""Module for hashing service implementation"""

__all__ = ['HashingService']

from typing import List
from typing import Optional

from fastapi import Depends

from services.hashing import IHashingService
from services.hashing.factories import HashingAlgorithmFactory
from services.hashing.factories import IHashingAlgorithmFactory
from entities.hashing_algorithms import IHashingAlgorithm
from dtos.hashes import HashesRequest
from dtos.hashes import HashesResponse
from dtos.hashes import map_algorithm_to_response


class HashingService(IHashingService):
    """Hashing service implementation

    Args:
        factory: Factory for creating hashing algorithms
    """

    def __init__(self, factory: IHashingAlgorithmFactory = Depends(HashingAlgorithmFactory)) -> None:
        self._factory = factory

    def hash_user_data(self, request: HashesRequest) -> Optional[HashesResponse]:
        """Hash user data

        Args:
            request: HashesRequest object with data

        Returns:
            HashesResponse with all needed data
        """

        algorithm: Optional[IHashingAlgorithm] = self._factory.create_algorithm(request.algorithm)
        if not algorithm:
            return None
        return map_algorithm_to_response(algorithm, algorithm.hash(request.data))

    def get_available_algorithms(self) -> List[str]:
        """Get available hashing algorithms

        Returns:
            A list with supported hashing algorihtms
        """

        return self._factory.get_available_algorithms()
