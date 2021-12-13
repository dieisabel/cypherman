from entities.hashing_algorithms import IHashingAlgorithm


class TestMD5HashingAlgorithm:
    def test_hash(self, md5: IHashingAlgorithm) -> None:
        # Arrange
        string: str = 'Hello, World!'
        expected: str = '65a8e27d8879283831b664bd8b7f0ad4'

        # Act
        actual: str = md5.hash(string)

        # Assert
        assert actual == expected
