import pytest

from typing import Optional, List

from app.services.hashing import IHashingService
from app.dtos.hashes import HashesRequest
from app.dtos.hashes import HashesResponse


class TestHashingService:
    def test_hash_user_data_with_md5(self, service: IHashingService) -> None:
        # Arrange
        request: HashesRequest = HashesRequest('Hello, World!')
        request.algorithm = 'md5'
        expected: HashesResponse = HashesResponse(
            algorithm='md5',
            bits=128,
            checksum='MD5 Hash',
            is_secure=False
        )

        # Act
        actual: Optional[HashesResponse] = service.hash_user_data(request)

        # Assert
        assert actual is not None
        assert actual.algorithm == expected.algorithm
        assert actual.bits == expected.bits
        assert actual.checksum == expected.checksum
        assert actual.is_secure == expected.is_secure


    def test_hash_user_data_with_sha1(self, service: IHashingService) -> None:
        # Arrange
        request: HashesRequest = HashesRequest('Hello, World!')
        request.algorithm = 'sha1'
        expected: HashesResponse = HashesResponse(
            algorithm='sha1',
            bits=160,
            checksum='SHA1 Hash',
            is_secure=False
        )

        # Act
        actual: Optional[HashesResponse] = service.hash_user_data(request)

        # Assert
        assert actual is not None
        assert actual.algorithm == expected.algorithm
        assert actual.bits == expected.bits
        assert actual.checksum == expected.checksum
        assert actual.is_secure == expected.is_secure


    def test_hash_user_data_with_non_supported_algorithm(self, service: IHashingService) -> None:
        # Arrange + Act
        request: HashesRequest = HashesRequest('Hello, World!')
        request.algorithm = 'sha256'
        actual: Optional[HashesResponse] = service.hash_user_data(request)

        # Assert
        assert actual is None

    def test_get_available_algorithms(self, service: IHashingService) -> None:
        # Arrange
        expected: List[str] = ['md5', 'sha1']

        # Act
        actual: List[str] = service.get_available_algorithms()

        # Assert
        assert actual == expected
