__all__ = ['router']

from fastapi import APIRouter

from api import v0

router = APIRouter(
    prefix='/api'
)

router.include_router(v0.router)
