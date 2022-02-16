"""Module for SHA256 hashing algorithm"""

__all__ = ['SHA256HashingAlgorithm']

import hashlib

from entities.hashing_algorithms import IHashingAlgorithm


class SHA256HashingAlgorithm(IHashingAlgorithm):
    """SHA256 hashing algorithm

    Attributes:
        name: Algorithm name
        bits: Amount of checksum bits
        is_secure: Can algorithm be used for securing purposes
    """

    name: str = "sha256"
    bits: int = 256
    is_secure: bool = True

    def hash(self, data: str) -> str:
        """Hash data with SHA256 hashing algorithm

        Args:
            data: Data to hash

        Returns:
            Checksum
        """

        encoded_data: bytes = data.encode('utf-8')
        return hashlib.sha256(encoded_data).hexdigest()
