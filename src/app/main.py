__all__ = ['application']

from fastapi import FastAPI

from api.v0.routers import hashes
from config import get_settings

settings = get_settings()

application = FastAPI(
    title=settings.APPLICATION_NAME,
    description=settings.APPLICATION_DESCRIPTION,
    version=settings.VERSION,
)

application.include_router(hashes.router)
