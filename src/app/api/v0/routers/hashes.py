"""Module for routes for hashing user data

Note:
    FastAPI can extract documentation from routes in Markdown and display it,
    so routes docstrings differs from other docstrings
"""

__all__ = ['router']

from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from services.hashing import IHashingService
from services.hashing import HashingService
from dtos import HashesDTO

router = APIRouter(
    prefix='/hashes',
)


@router.get('')
async def get_available_hashing_algorithms(
    service: IHashingService = Depends(HashingService)
) -> List[str]:
    """Display a list that contains supported hashing algorithms"""
    return service.get_available_algorithms()


@router.post('/{algorithm}/hash')
async def hash_user_data(
    request: HashesDTO.Request,
    algorithm: str,
    service: IHashingService = Depends(HashingService)
) -> HashesDTO.Response:
    """
    Hash user data

    - **algorithm** - Hashing algorithm to use
    - **data** - User data
    """

    request.set_algorithm(algorithm)
    result: Optional[HashesDTO.Response] = service.hash_user_data(request)
    if not result:
        raise HTTPException(status_code=404, detail='Algorithm is not supported')
    return result
