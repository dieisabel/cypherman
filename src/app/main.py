__all__ = ['application']

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api import router
from core.config import get_config
from core.db.initialize import initialize_database
from services.users.exceptions import UserNotFoundException
from services.users.exceptions import UserIsExistsException

settings = get_config()

initialize_database()

application = FastAPI(
    title=settings.APPLICATION_NAME,
    description=settings.APPLICATION_DESCRIPTION,
    version=settings.VERSION,
)

application.include_router(router)


@application.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(request, exception):
    return JSONResponse(
        status_code=404,
        content={
            'message': exception.message
        }
    )


@application.exception_handler(UserIsExistsException)
def user_is_exists_exception_handler(request, exception):
    return JSONResponse(
        status_code=404,
        content={
            'message': exception.message
        }
    )


