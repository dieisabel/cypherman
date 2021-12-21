__all__ = ['router']

from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from services.hashing import IHashingService, HashingService
from dtos import HashesDTO

router = APIRouter(
    prefix='/hashes',
)


@router.get('')
async def get_available_hashing_algorithms(
    service: IHashingService = Depends(HashingService)
) -> List[str]:
    return service.get_available_algorithms()


@router.post('/{algorithm}/hash')
async def hash_user_data(
    request: HashesDTO.Request,
    algorithm: str,
    service: IHashingService = Depends(HashingService)
) -> HashesDTO.Response:
    request.set_algorithm(algorithm)
    result: Optional[HashesDTO.Response] = service.hash_user_data(request)
    if not result:
        raise HTTPException(status_code=404, detail='Algorithm is not supported')
    return result
