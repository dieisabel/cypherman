__all__ = ['HashingServiceMock']

from typing import List, Optional

from app.dtos import HashesDTO
from app.services.hashing import IHashingService


class HashingServiceMock(IHashingService):
    def hash_user_data(self, request: HashesDTO.Request) -> Optional[HashesDTO.Response]:
        if request.algorithm == 'md5':
            return HashesDTO.Response(
                algorithm='md5',
                bits=128,
                checksum='MD5 Hash',
                is_secure=False
            )
        if request.algorithm == 'sha1':
            return HashesDTO.Response(
                algorithm='sha1',
                bits=160,
                checksum='SHA1 Hash',
                is_secure=False
            )
        return None

    def get_available_algorithms(self) -> List[str]:
        return ['md5']
