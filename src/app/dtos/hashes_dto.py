"""Module for hashes data transfer objects"""

__all__ = ['HashesDTO']

from dataclasses import dataclass


@dataclass
class HashesDTO:

    @dataclass
    class Request:
        data: str

        def set_algorithm(self, algorithm: str):
            self.algorithm = algorithm

    @dataclass
    class Response:
        algorithm: str
        bits: int
        checksum: str
        is_secure: bool
