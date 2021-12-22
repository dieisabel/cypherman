__all__ = ['SHA1HashingAlgorithm']

import hashlib

from entities.hashing_algorithms import IHashingAlgorithm


class SHA1HashingAlgorithm(IHashingAlgorithm):
    name: str = "sha1"
    bits: int = 160
    is_secure: bool = False

    def hash(self, data: str) -> str:
        """Hash data with SHA1 hashing algorithm

        :param data: Data to hash
        :return: Checksum
        """

        encoded_data: bytes = data.encode('utf-8')
        return hashlib.sha1(encoded_data).hexdigest()
