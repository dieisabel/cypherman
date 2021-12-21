__all__ = ['application']

from fastapi import FastAPI

from api.v0.routers import hashes

application = FastAPI()

application.include_router(hashes.router)
