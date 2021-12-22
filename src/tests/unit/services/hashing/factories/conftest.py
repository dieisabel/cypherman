from typing import Dict

import pytest
from pytest_mock import MockerFixture

from app.entities.hashing_algorithms import IHashingAlgorithm
from app.services.hashing.factories import IHashingAlgorithmFactory, HashingAlgorithmFactory
from tests.unit.services.hashing.factories import mocks


@pytest.fixture
def factory(mocker: MockerFixture) -> IHashingAlgorithmFactory:
    obj: IHashingAlgorithmFactory = HashingAlgorithmFactory()
    mock_registry: Dict[str, IHashingAlgorithm] = {    # type: ignore
        'md5': mocks.MD5HashingAlgorithmMock,
        'sha1': mocks.SHA1HashingAlgorithmMock,
    }
    mocker.patch.object(obj, '_registry', mock_registry)
    return obj
