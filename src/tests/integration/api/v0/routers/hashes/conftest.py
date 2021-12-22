import pytest
from fastapi.testclient import TestClient

from app.main import application
from app.services.hashing import HashingService, IHashingService
from tests.integration.api.v0.routers.hashes.mocks import HashingServiceMock


async def mock_hashing_service() -> IHashingService:
    return HashingServiceMock()


application.dependency_overrides[HashingService] = mock_hashing_service


@pytest.fixture
def client() -> TestClient:
    return TestClient(application)
