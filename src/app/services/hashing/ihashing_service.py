__all__ = ['IHashingService']

from abc import ABC, abstractmethod
from typing import List, Optional

from schemas import HashesDTO


class IHashingService(ABC):

    # TODO: Maybe we should use HashesRequest or some sort of DTO as argument
    @abstractmethod
    def hash_user_data(self, data: str, algorithm_name: str) -> Optional[HashesDTO]:
        raise NotImplementedError

    def get_available_algorithms(self) -> List[str]:
        raise NotImplementedError
