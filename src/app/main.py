__all__ = ['application']

from fastapi import FastAPI

from api import router
from core.config import get_config
from core.db import start_mappers

settings = get_config()

start_mappers()

application = FastAPI(
    title=settings.APPLICATION_NAME,
    description=settings.APPLICATION_DESCRIPTION,
    version=settings.VERSION,
)

application.include_router(router)
