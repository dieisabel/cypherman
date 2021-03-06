"""Module for configuration dependencies, which can be used in client code"""

__all__ = ['get_config']

import os
from typing import Dict
from typing import Type
from typing import Optional
from functools import lru_cache

from core.config.base import Config
from core.config.development import DevelopmentConfig
from core.config.testing import TestingConfig
from core.config.production import ProductionConfig
from core.exceptions import ImproperlyConfigured


@lru_cache
def get_config() -> Config:
    """Get current application configuration

    Looks at FASTAPI_CONFIGURATION environment variable to determine what configuration to use.

    Returns:
        Current application configuration

    Raises:
        ImproperlyConfigured: FASTAPI_CONFIGURATION environ is not set or configuration is not in registry.
    """

    return _get_config(_get_config_registry())


def _get_config(registry: Dict[str, Type[Config]]) -> Config:
    config_environ: Optional[str] = os.environ.get('FASTAPI_CONFIGURATION', None)
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
