__all__ = ['SHA256HashingAlgorithm']

import hashlib

from entities.hashing_algorithms import IHashingAlgorithm


class SHA256HashingAlgorithm(IHashingAlgorithm):
    name: str = "sha256"
    bits: int = 256
    is_secure: bool = True

    def hash(self, data: str) -> str:
        encoded_data: bytes = data.encode('utf-8')
        return hashlib.sha256(encoded_data).hexdigest()
