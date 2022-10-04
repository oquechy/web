from concurrent.futures import ThreadPoolExecutor

import grpc

from grpc_logger.definitions.builds.service_pb2 import Null
from grpc_logger.definitions.builds.service_pb2_grpc import \
    LogServiceServicer, \
    add_LogServiceServicer_to_server


class Service(LogServiceServicer):
    def Log(self, request, _):
        print(request.msg)
        return Null()


def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_LogServiceServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
