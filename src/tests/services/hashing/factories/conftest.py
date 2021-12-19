from typing import Dict

import pytest
from pytest_mock import MockerFixture

from services.hashing.factories import IHashingAlgorithmFactory, HashingAlgorithmFactory
from tests.services.hashing.factories import mocks


@pytest.fixture
def factory(mocker: MockerFixture) -> IHashingAlgorithmFactory:
    obj: IHashingAlgorithmFactory = HashingAlgorithmFactory()
    mock_registry: Dict[str, IHashingAlgorithmFactory] = {    # type: ignore
        'md5': mocks.MD5HashingAlgorithmMock,
        'sha1': mocks.SHA1HashingAlgorithmMock,
    }
    mocker.patch.object(obj, '_registry', mock_registry)
    return obj
