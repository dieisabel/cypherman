__all__ = ['application']

from fastapi import FastAPI

from api import router
from core.config import get_config
from core.db.initialize import initialize_database

settings = get_config()

initialize_database()

application = FastAPI(
    title=settings.APPLICATION_NAME,
    description=settings.APPLICATION_DESCRIPTION,
    version=settings.VERSION,
)

application.include_router(router)
