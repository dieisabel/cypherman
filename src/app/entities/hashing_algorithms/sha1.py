"""Module for SHA1 hashing algorithm"""

__all__ = ['SHA1HashingAlgorithm']

import hashlib

from entities.hashing_algorithms import IHashingAlgorithm


class SHA1HashingAlgorithm(IHashingAlgorithm):
    """SHA1 hashing algorithm

    Attributes:
        name: Algorithm name
        bits: Amount of checksum bits
        is_secure: Can algorithm be used for securing purposes
    """

    name: str = "sha1"
    bits: int = 160
    is_secure: bool = False

    def hash(self, data: str) -> str:
        """Hash data with SHA1 hashing algorithm

        Args:
            data: Data to hash

        Returns:
            Checksum
        """

        encoded_data: bytes = data.encode('utf-8')
        return hashlib.sha1(encoded_data).hexdigest()
