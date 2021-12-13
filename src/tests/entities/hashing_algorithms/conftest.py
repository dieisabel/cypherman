import pytest

from entities.hashing_algorithms import IHashingAlgorithm, MD5HashingAlgorithm


@pytest.fixture
def md5() -> IHashingAlgorithm:
    return MD5HashingAlgorithm()
