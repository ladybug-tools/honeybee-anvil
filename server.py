from concurrent import futures
import time
import grpc

# from helloworld import HelloWorldService
from honeybee_server import HoneybeeService
from service import MicroserviceService
from servicemanager import ServiceManagerService


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    HoneybeeService.add_to_server(server)
    MicroserviceService.add_to_server(server)
    ServiceManagerService.add_to_server(server)

    port = '[::]:50001'
    print('Starting Honeybee Service on ' + port)
    server.add_insecure_port(port)
    server.start()

    try:
        while True:
            time.sleep(3600 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
