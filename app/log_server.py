from concurrent.futures import ThreadPoolExecutor

import os.path
from pathlib import Path

import grpc

from grpc_logger.definitions.builds.service_pb2 import Null
from grpc_logger.definitions.builds.service_pb2_grpc import \
    LogServiceServicer, \
    add_LogServiceServicer_to_server


class Service(LogServiceServicer):
    def Log(self, request, _):
        prefix = "out"
        Path(prefix).mkdir(parents=True, exist_ok=True)
        with open(os.path.join(prefix, "log"), "a") as f:
            match request.lvl:
                case 1:
                    print("INFO", request.msg, file=f)
                case 2:
                    print("ERRO", request.msg, file=f)
                case _:
                    print("????", request.msg, file=f)
        return Null()


def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_LogServiceServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    print("The log server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
