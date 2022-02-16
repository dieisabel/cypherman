"""Module for MD5 hashing algorithm"""

__all__ = ['MD5HashingAlgorithm']

import hashlib

from entities.hashing_algorithms import IHashingAlgorithm


class MD5HashingAlgorithm(IHashingAlgorithm):
    """MD5 hashing algorithm

    Attributes:
        name: Algorithm name
        bits: Amount of checksum bits
        is_secure: Can algorithm be used for securing purposes
    """

    name: str = "md5"
    bits: int = 128
    is_secure: bool = False

    def hash(self, data: str) -> str:
        """Hash data with MD5 hashing algorithm

        Args:
            data: Data to hash

        Returns:
            Checksum
        """

        encoded_data: bytes = data.encode('utf-8')
        return hashlib.md5(encoded_data).hexdigest()
