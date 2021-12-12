__all__ = ['IHashingAlgorithm']

from abc import ABC, abstractmethod


class IHashingAlgorithm(ABC):

    # TODO: Should we use checksum property instead of hash method?
    @abstractmethod
    def hash(self, data: str) -> str:
        raise NotImplementedError
