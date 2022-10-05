from enum import Enum

import grpc
from .grpc_logger.definitions.builds.service_pb2 import Msg
from .grpc_logger.definitions.builds.service_pb2_grpc import LogServiceStub


class Level(int, Enum):
    INFO = 1
    ERRO = 2


def log(lvl: Level, msg: str):
    logger = LogServiceStub(grpc.insecure_channel("localhost:3000"))
    logger.Log(Msg(lvl=lvl, msg=msg))
