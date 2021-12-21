from typing import Optional, List

from services.hashing import IHashingService
from dtos import HashesDTO


class TestHashingService:
    def test_hash_user_data_with_md5(self, service: IHashingService) -> None:
        # Arrange
        request: HashesDTO.Request = HashesDTO.Request(data='Hello, World!')
        request.set_algorithm('md5')
        expected: HashesDTO.Response = HashesDTO.Response(
            algorithm='md5',
            bits=128,
            checksum='MD5 Hash',
            is_secure=False
        )

        # Act
        actual: Optional[HashesDTO.Response] = service.hash_user_data(request)

        # Assert
        assert actual == expected

    def test_hash_user_data_with_sha1(self, service: IHashingService) -> None:
        # Arrange
        request: HashesDTO.Request = HashesDTO.Request(data='Hello, World!')
        request.set_algorithm('sha1')
        expected: HashesDTO.Response = HashesDTO.Response(
            algorithm='sha1',
            bits=160,
            checksum='SHA1 Hash',
            is_secure=False
        )

        # Act
        actual: Optional[HashesDTO.Response] = service.hash_user_data(request)

        # Assert
        assert actual == expected

    def test_hash_user_data_with_non_supported_algorithm(self, service: IHashingService) -> None:
        # Arrange + Act
        request: HashesDTO.Request = HashesDTO.Request(data='Hello, World!')
        request.set_algorithm('sha256')
        actual: Optional[HashesDTO.Response] = service.hash_user_data(request)

        # Assert
        assert actual is None

    def test_get_available_algorithms(self, service: IHashingService) -> None:
        # Arrange
        expected: List[str] = ['md5', 'sha1']

        # Act
        actual: List[str] = service.get_available_algorithms()

        # Assert
        assert actual == expected
