__all__ = ['SHA1HashingAlgorithmMock']

from entities.hashing_algorithms import IHashingAlgorithm


class SHA1HashingAlgorithmMock(IHashingAlgorithm):
    def hash(self, data: str) -> str:
        return 'SHA1 Hash'
