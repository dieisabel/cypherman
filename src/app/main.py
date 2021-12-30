__all__ = ['application']

from fastapi import FastAPI

from api import router
from core.config import get_config

settings = get_config()

application = FastAPI(
    title=settings.APPLICATION_NAME,
    description=settings.APPLICATION_DESCRIPTION,
    version=settings.VERSION,
)

application.include_router(router)
