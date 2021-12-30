__all__ = ['get_config']

from typing import Dict, Type, Optional
from functools import lru_cache
import os

from config.base import Config
from config.development import DevelopmentConfig
from config.testing import TestingConfig
from config.production import ProductionConfig
from config.exceptions import ImproperlyConfigured


@lru_cache
def get_config() -> Config:
    """Get current application configuration

    To get a configuration function looks at the FASTAPI_CONFIGURATION environ and configuration registry.

    :raises ImproperlyConfigured: FASTAPI_CONFIGURATION environ is not set or configuration is not in registry.
    :return: Current application configuration
    """
    return _get_config(_get_config_registry())


def _get_config(registry: Dict[str, Type[Config]]) -> Config:
    config_environ: str = os.environ.get('FASTAPI_CONFIGURATION', None)
    if not config_environ:
        raise ImproperlyConfigured('Application configuration is not set. Set FASTAPI_CONFIGURATION environ.')

    config_class: Optional[Type[Config]] = registry.get(config_environ.lower(), None)
    if not config_class:
        raise ImproperlyConfigured(f'{config_environ.lower()} config not found')

    return config_class()


def _get_config_registry() -> Dict[str, Type[Config]]:
    return {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
    }
