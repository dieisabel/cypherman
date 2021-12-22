import pytest
from fastapi.testclient import TestClient

from main import application
from services.hashing import HashingService, IHashingService
from tests.api.v0.routers.hashes.mocks import HashingServiceMock


async def mock_hashing_service() -> IHashingService:
    return HashingServiceMock()


application.dependency_overrides[HashingService] = mock_hashing_service


@pytest.fixture
def client() -> TestClient:
    return TestClient(application)
