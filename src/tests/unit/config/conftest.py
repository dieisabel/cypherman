import pytest

from core.config import get_config


@pytest.fixture(autouse=True)
def clear_get_config_cache() -> None:
    get_config.cache_clear()
