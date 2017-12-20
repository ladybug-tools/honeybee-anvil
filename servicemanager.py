from anvilCore import servicemanager_pb2
from anvilCore import servicemanager_pb2_grpc

class ServiceManagerService(servicemanager_pb2_grpc.ServiceManagerServicer):

    @classmethod
    def add_to_server(cls, server):
        servicemanager_pb2_grpc.add_ServiceManagerServicer_to_server(ServiceManagerService(), server)