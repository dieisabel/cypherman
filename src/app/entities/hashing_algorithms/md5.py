__all__ = ['MD5HashingAlgorithm']

import hashlib

from entities.hashing_algorithms import IHashingAlgorithm


class MD5HashingAlgorithm(IHashingAlgorithm):
    name: str = "md5"
    bits: int = 128
    is_secure: bool = False

    def hash(self, data: str) -> str:
        encoded_data: bytes = data.encode('utf-8')
        return hashlib.md5(encoded_data).hexdigest()
