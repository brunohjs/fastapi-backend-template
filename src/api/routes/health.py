from http import HTTPStatus

import fastapi
from fastapi.responses import JSONResponse


router = fastapi.APIRouter()


@router.get("/health", summary="Health check")
async def heartbeat():
    return JSONResponse(
        status_code=fastapi.status.HTTP_200_OK,
        content={"message": HTTPStatus(fastapi.status.HTTP_200_OK).phrase},
    )
