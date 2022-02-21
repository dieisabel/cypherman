__all__ = ['HashingServiceMock']

from typing import List, Optional

from app.dtos.hashes import HashesRequest
from app.dtos.hashes import HashesResponse
from app.services.hashing import IHashingService


class HashingServiceMock(IHashingService):
    def hash_user_data(self, request: HashesRequest) -> Optional[HashesResponse]:
        if request.algorithm == 'md5':
            return HashesResponse(
                algorithm='md5',
                bits=128,
                checksum='MD5 Hash',
                is_secure=False
            )
        if request.algorithm == 'sha1':
            return HashesResponse(
                algorithm='sha1',
                bits=160,
                checksum='SHA1 Hash',
                is_secure=False
            )
        return None

    def get_available_algorithms(self) -> List[str]:
        return ['md5', 'sha1']
