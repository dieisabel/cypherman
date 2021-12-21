__all__ = ['IHashingService']

from abc import ABC, abstractmethod
from typing import List, Optional

from dtos import HashesDTO


class IHashingService(ABC):

    @abstractmethod
    def hash_user_data(self, request: HashesDTO.Request) -> Optional[HashesDTO.Response]:
        raise NotImplementedError

    def get_available_algorithms(self) -> List[str]:
        raise NotImplementedError
