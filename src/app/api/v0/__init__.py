__all__ = ['router']

from fastapi import APIRouter

from api.v0.routers import hashes

router = APIRouter(
    prefix='/v0'
)

router.include_router(hashes.router)
