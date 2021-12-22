from app.entities.hashing_algorithms import IHashingAlgorithm


class TestSHA1HashingAlgorithm:
    def test_hash(self, sha1: IHashingAlgorithm) -> None:
        # Arrange
        string: str = 'Hello, World!'
        expected: str = '0a0a9f2a6772942557ab5355d76af442f8f65e01'

        # Act
        actual: str = sha1.hash(string)

        # Assert
        assert actual == expected
