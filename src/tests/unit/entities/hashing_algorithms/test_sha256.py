from app.entities.hashing_algorithms import IHashingAlgorithm


class TestSHA256HashingAlgorithm:
    def test_hash(self, sha256: IHashingAlgorithm) -> None:
        # Arrange
        string: str = 'Hello, World!'
        expected: str = 'dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f'

        # Act
        actual: str = sha256.hash(string)

        # Assert
        assert actual == expected
