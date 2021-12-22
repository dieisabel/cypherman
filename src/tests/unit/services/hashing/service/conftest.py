import pytest

from app.services.hashing import IHashingService, HashingService
from tests.unit.services.hashing.service.mocks import HashingAlgorithmFactoryMock


@pytest.fixture
def service() -> IHashingService:
    factory_mock = HashingAlgorithmFactoryMock()
    return HashingService(factory_mock)
