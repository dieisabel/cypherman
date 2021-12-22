__all__ = ['MD5HashingAlgorithmMock']

from app.entities.hashing_algorithms import IHashingAlgorithm


class MD5HashingAlgorithmMock(IHashingAlgorithm):
    name: str = "md5"
    bits: int = 128
    is_secure: bool = False

    def hash(self, data: str) -> str:
        return 'MD5 Hash'
