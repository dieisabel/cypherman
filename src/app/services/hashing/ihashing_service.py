__all__ = ['IHashingService']

from abc import ABC, abstractmethod
from typing import List, Optional

from dtos import HashesDTO


class IHashingService(ABC):

    @abstractmethod
    def hash_user_data(self, request: HashesDTO.Request) -> Optional[HashesDTO.Response]:
        """Hash user data

        :param request: A request object that contains data and algorithm to use
        :return: HashesDTO with all needed data: algorithm, bits, checksum and is_secure flag
        """

        raise NotImplementedError

    @abstractmethod
    def get_available_algorithms(self) -> List[str]:
        """Get available hashing algorithms

        :return: A list which contains supported hashing algorithms
        """

        raise NotImplementedError
