from fastapi import APIRouter
from fastapi.responses import FileResponse

import grpc
from ..grpc_logger.definitions.builds.service_pb2 import Msg
from ..grpc_logger.definitions.builds.service_pb2_grpc import LogServiceStub

LOGGER = LogServiceStub(grpc.insecure_channel("localhost:3000"))

router = APIRouter()

favicon_path = 'favicon.ico'


@router.get('/favicon.ico')
async def favicon() -> FileResponse:
    """Returns the favicon.

    Returns:
        FileResponse: Image.
    """
    LOGGER.Log(Msg(lvl=1, msg="fetch favicon"))
    return FileResponse(favicon_path)
