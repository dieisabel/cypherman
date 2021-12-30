import pytest
from pytest_mock import MockerFixture

from core.config import Config, get_config
from core.exceptions import ImproperlyConfigured
from tests.unit.config.mocks import ConfigMock


class TestDependencies:
    def test_get_config_with_environ_and_config_in_registry(self, mocker: MockerFixture) -> None:
        # Arrange
        expected: Config = ConfigMock()
        mocker.patch('core.config.dependencies._get_config_registry', return_value={'mock': ConfigMock})
        mocker.patch('os.environ', {'FASTAPI_CONFIGURATION': 'MOCK'})

        # Act
        actual: Config = get_config()

        # Assert
        assert actual.__class__ == expected.__class__

    def test_get_config_without_environ_and_config_in_registry(self, mocker: MockerFixture) -> None:
        # Arrange
        mocker.patch('core.config.dependencies._get_config_registry', return_value={'mock': ConfigMock})
        mocker.patch('os.environ', {})

        # Act + Assert
        with pytest.raises(ImproperlyConfigured):
            actual: Config = get_config()

    def test_get_config_with_environ_and_config_not_in_registry(self, mocker: MockerFixture) -> None:
        # Arrange
        mocker.patch('core.config.dependencies._get_config_registry', return_value={})
        mocker.patch('os.environ', {'FASTAPI_CONFIGURATION': 'mock'})

        # Act + Assert
        with pytest.raises(ImproperlyConfigured):
            actual: Config = get_config()

    # TODO: Is this test is needed?
    # We already tested behaviour with and without environ or with and without configuration in registry
    def test_get_config_without_environ_and_config_not_in_registry(self, mocker: MockerFixture) -> None:
        # Arrange
        mocker.patch('core.config.dependencies._get_config_registry', return_value={})
        mocker.patch('os.environ', {})

        # Act + Assert
        with pytest.raises(ImproperlyConfigured):
            actual: Config = get_config()
