__all__ = ['SHA1HashingAlgorithmMock']

from app.entities.hashing_algorithms import IHashingAlgorithm


class SHA1HashingAlgorithmMock(IHashingAlgorithm):
    name: str = "sha1"
    bits: int = 160
    is_secure: bool = False

    def hash(self, data: str) -> str:
        return 'SHA1 Hash'
