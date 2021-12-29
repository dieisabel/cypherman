__all__ = ['get_config']

from typing import Dict, Type, Optional
from functools import lru_cache
import os

from config.base import Config
from config.development import DevelopmentConfig
from config.testing import TestingConfig


@lru_cache()
def get_config() -> Config:
    config_environ: str = os.environ.get('FASTAPI_CONFIGURATION')
    if not config_environ:
        raise Exception('Application configuration is not set')

    config_registry: Dict[str, Type[Config]] = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
    }
    config_class: Optional[Type[Config]] = config_registry.get(config_environ.lower())
    if not config_class:
        raise Exception('Config not found')

    return config_class()