from fastapi import APIRouter

from typing import Union

from pydantic import BaseModel

import app.db as db

import grpc
from ..grpc_logger.definitions.builds.service_pb2 import Msg
from ..grpc_logger.definitions.builds.service_pb2_grpc import LogServiceStub

LOGGER = LogServiceStub(grpc.insecure_channel("localhost:3000"))

router = APIRouter()


class Closet(BaseModel):
    description: Union[str, None] = None
    closet_size: int
    winter_looks: int
    summer_looks: int


@router.get("/")
async def main() -> Closet:
    """Returns information about size of the closet and number of possible 
    outfits.

    Returns:
        Closet: Info record.
    """
    resp = Closet(
        description="Welcome to my web closet!! (^o^)/",
        closet_size=len(db.closet()),
        summer_looks=db.summer_looks(),
        winter_looks=db.winter_looks(),
    )
    LOGGER.Log(Msg(msg="fetch stats"))
    return resp
