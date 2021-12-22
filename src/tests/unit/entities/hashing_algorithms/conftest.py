import pytest

from app.entities.hashing_algorithms import (
    IHashingAlgorithm,
    MD5HashingAlgorithm,
    SHA1HashingAlgorithm,
    SHA256HashingAlgorithm,
)


@pytest.fixture
def md5() -> IHashingAlgorithm:
    return MD5HashingAlgorithm()


@pytest.fixture
def sha1() -> IHashingAlgorithm:
    return SHA1HashingAlgorithm()


@pytest.fixture
def sha256() -> IHashingAlgorithm:
    return SHA256HashingAlgorithm()
