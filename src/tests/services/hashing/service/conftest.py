import pytest

from services.hashing import IHashingService, HashingService
from tests.services.hashing.service.mocks import HashingAlgorithmFactoryMock


@pytest.fixture
def service() -> IHashingService:
    factory_mock = HashingAlgorithmFactoryMock()
    return HashingService(factory_mock)
