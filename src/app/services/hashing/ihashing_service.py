"""Module for hashing service interface"""

__all__ = ['IHashingService']

from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Optional

from dtos.hashes import HashesRequest
from dtos.hashes import HashesResponse


class IHashingService(ABC):
    """Hashing service interface"""

    @abstractmethod
    def hash_user_data(self, request: HashesRequest) -> Optional[HashesResponse]:
        """Hash user data

        Args:
            request: HashesRequest object with data

        Returns:
            HashesResponse with all needed data
        """

        raise NotImplementedError

    @abstractmethod
    def get_available_algorithms(self) -> List[str]:
        """Get available hashing algorithms

        Returns:
            A list with supported hashing algorihtms
        """

        raise NotImplementedError
