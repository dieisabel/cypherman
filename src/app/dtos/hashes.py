"""Module for hashes data transfer objects and its mappers"""

__all__ = [
    'HashesRequest',
    'HashesResponse',
    'map_algorithm_to_response',
]

from dataclasses import dataclass
from typing import Optional

from entities.hashing_algorithms import IHashingAlgorithm


@dataclass
class HashesRequest:
    """Hashes request

    Object for transfering data from hashes controllers to a HashingService.
    There no mapper for mapping HashesRequest to HashingAlgorithm because there are factory, that
    produces algorithm by its name, so there no meaning of mapper.

    Warning:
        HashingService needs algorithm name, but we get this from url path parameter, so don't forget to set
        algorithm attribute by yourself. So, if you don't set there will be an error.

    Args:
        data: Data to hash
        algorithm: You can provide algorithm
    """

    data: str
    algorithm: Optional[str] = None


@dataclass
class HashesResponse:
    """Hashes response

    Object for transfering data from HashingService to hashes controllers.
    To map HashingAlgorithm to HashesResponse use map_algorithm_to_response function.

    Args:
        algorithm: Algorithm name
        bits: Amount of checksum bits
        checksum: Checksum
        is_secure: Can algorithm be user for securing purposes
    """

    algorithm: str
    bits: int
    checksum: str
    is_secure: bool


def map_algorithm_to_response(algorithm: IHashingAlgorithm, checksum: str) -> HashesResponse:
    """Map hashing algorithm to hashes response

    Mappers and dtos cant contain logic, but mapper needs checksum to generate a response. So, you need
    to hash data somewhere else and provide checksum to a mapper

    Args:
        algorithm: Hashing algorithm
        checksum: Hash checksum
    """

    return HashesResponse(
        algorithm=algorithm.name,
        bits=algorithm.bits,
        checksum=checksum,
        is_secure=algorithm.is_secure,
    )
