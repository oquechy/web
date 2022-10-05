from fastapi import APIRouter
from fastapi.responses import FileResponse

import os

from app.collage import make_collage, save_collage
import app.db as db

import grpc
from ..grpc_logger.definitions.builds.service_pb2 import Msg
from ..grpc_logger.definitions.builds.service_pb2_grpc import LogServiceStub

LOGGER = LogServiceStub(grpc.insecure_channel("localhost:3000"))

router = APIRouter()


@router.get("/closet")
async def closet() -> FileResponse:
    """Creates a collage from all wardrobe items.

    Returns:
        FileResponse: Image.
    """
    pic = make_collage(db.closet())

    prefix = os.path.join("out", "closet")
    path = save_collage(pic, prefix)
    LOGGER.Log(Msg(lvl=1, msg="fetch closet"))
    return FileResponse(path)
