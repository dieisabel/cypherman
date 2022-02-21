from typing import Dict, Any, List

from fastapi.testclient import TestClient
from requests import Response


class TestHashesControllers:
    def test_hash_user_data_with_md5(self, client: TestClient) -> None:
        # Arrange
        expected: Dict[str, Any] = {
            'algorithm': 'md5',
            'bits': 128,
            'checksum': 'MD5 Hash',
            'is_secure': False,
        }
        body: Dict[str, Any] = {'data': 'Hello, World!'}

        # Act
        response: Response = client.post('/api/v0/hashes/md5/hash', json=body)

        # Assert
        assert response.status_code == 200
        assert response.json() == expected

    def test_hash_user_data_with_sha1(self, client: TestClient) -> None:
        # Arrange
        expected: Dict[str, Any] = {
            'algorithm': 'sha1',
            'bits': 160,
            'checksum': 'SHA1 Hash',
            'is_secure': False,
        }
        body: Dict[str, Any] = {'data': 'Hello, World!'}

        # Act
        response: Response = client.post('/api/v0/hashes/sha1/hash', json=body)

        # Assert
        assert response.status_code == 200
        assert response.json() == expected

    def test_hash_user_data_with_non_supported_algorithm(self, client: TestClient) -> None:
        # Arrange
        expected: Dict[str, Any] = {'detail': 'sha256 is not supported'}
        body: Dict[str, Any] = {'data': 'Hello, World!'}

        # Act
        response = client.post('/api/v0/hashes/sha256/hash', json=body)

        # Assert
        assert response.status_code == 404
        assert response.json() == expected

    def test_get_available_algorithms(self, client: TestClient) -> None:
        # Arrange
        expected: List[str] = ['md5', 'sha1']

        # Act
        response: Response = client.get('/api/v0/hashes')

        # Assert
        assert response.status_code == 200
        assert response.json() == expected
