__all__ = ['MD5HashingAlgorithmMock']

from app.entities.hashing_algorithms import IHashingAlgorithm


class MD5HashingAlgorithmMock(IHashingAlgorithm):
    def hash(self, data: str) -> str:
        return 'MD5 Hash'
