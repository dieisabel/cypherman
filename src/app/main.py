__all__ = ['application']

from fastapi import FastAPI

from api import router
from config import get_settings

settings = get_settings()

application = FastAPI(
    title=settings.APPLICATION_NAME,
    description=settings.APPLICATION_DESCRIPTION,
    version=settings.VERSION,
)

application.include_router(router)
