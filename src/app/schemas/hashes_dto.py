__all__ = ['HashesDTO']

from dataclasses import dataclass


@dataclass
class HashesDTO:
    algorithm: str
    bits: int
    checksum: str
    is_secure: bool
