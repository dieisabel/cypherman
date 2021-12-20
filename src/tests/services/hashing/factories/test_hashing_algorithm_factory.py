from typing import Optional, List

from tests.services.hashing.factories import mocks
from services.hashing.factories import IHashingAlgorithmFactory
from entities.hashing_algorithms import IHashingAlgorithm


class TestHashingAlgorithmFactory:
    def test_create_md5_algorithm(self, factory: IHashingAlgorithmFactory) -> None:
        # Arrange
        expected: IHashingAlgorithm = mocks.MD5HashingAlgorithmMock()

        # Act
        actual: Optional[IHashingAlgorithm] = factory.create_algorithm('md5')

        # Assert
        assert actual.__class__ == expected.__class__

    def test_create_sha1_algorithm(self, factory: IHashingAlgorithmFactory) -> None:
        # Arrange
        expected: IHashingAlgorithm = mocks.SHA1HashingAlgorithmMock()

        # Act
        actual: Optional[IHashingAlgorithm] = factory.create_algorithm('sha1')

        # Assert
        assert actual.__class__ == expected.__class__

    def test_create_non_supported_algorithm(self, factory: IHashingAlgorithmFactory) -> None:
        # Arrange + Act
        actual: Optional[IHashingAlgorithm] = factory.create_algorithm('sha256')

        # Assert
        assert actual is None

    def test_get_available_algorithms(self, factory: IHashingAlgorithmFactory) -> None:
        # Arrange
        expected: List[str] = ['md5', 'sha1']

        # Act
        actual: List[str] = factory.get_available_algorithms()

        # Assert
        assert actual == expected
