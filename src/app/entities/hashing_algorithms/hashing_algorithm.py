__all__ = ['IHashingAlgorithm']

from abc import ABC, abstractmethod


class IHashingAlgorithm(ABC):
    name: str
    bits: int
    is_secure: bool

    # TODO: Should we use checksum property instead of hash method?
    @abstractmethod
    def hash(self, data: str) -> str:
        """Hash data

        :param data: Data to hash
        :return: Checksum
        """

        raise NotImplementedError
