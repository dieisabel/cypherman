from typing import Optional, List

from services.hashing import IHashingService
from schemas import HashesDTO


class TestHashingService:
    def test_hash_user_data_with_md5(self, service: IHashingService) -> None:
        # Arrange
        expected: HashesDTO = HashesDTO(
            algorithm='md5',
            bits=128,
            checksum='MD5 Hash',
            is_secure=False
        )

        # Act
        actual: Optional[HashesDTO] = service.hash_user_data('Hello, World!', 'md5')

        # Assert
        assert actual == expected

    def test_hash_user_data_with_sha1(self, service: IHashingService) -> None:
        # Arrange
        expected: HashesDTO = HashesDTO(
            algorithm='sha1',
            bits=160,
            checksum='SHA1 Hash',
            is_secure=False
        )

        # Act
        actual: Optional[HashesDTO] = service.hash_user_data('Hello, World!', 'sha1')

        # Assert
        assert actual == expected

    def test_hash_user_data_with_non_supported_algorithm(self, service: IHashingService) -> None:
        # Arrange + Act
        actual: Optional[HashesDTO] = service.hash_user_data('Hello, World!', 'sha256')

        # Assert
        assert actual is None

    def test_get_available_algorithms(self, service: IHashingService) -> None:
        # Arrange
        expected: List[str] = ['md5', 'sha1']

        # Act
        actual: List[str] = service.get_available_algorithms()

        # Assert
        assert actual == expected
