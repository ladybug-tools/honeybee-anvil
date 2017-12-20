from anvilCore import service_pb2
from anvilCore import service_pb2_grpc

root = "proto/"

class MicroserviceService(service_pb2_grpc.MicroserviceServicer):
    
    @classmethod
    def add_to_server(cls, server):
        service_pb2_grpc.add_MicroserviceServicer_to_server(MicroserviceService(), server)

    def Description(self, request, context):
        return service_pb2.DescriptionResponse(
            company_name='Ladybug', 
            service_name='Honeybee',
            service_description='Honeybee Daylight Simulator Microservice'
        )

    def Files(self, request, context):
        paths = ['honeybee.proto']
        filedata = []
        for filename in paths:
            with open(root + filename, 'rb') as myfile:
                bytes = myfile.read()
                filedata.append(service_pb2.File(path=filename, contents=bytes))
        return service_pb2.FileResponse(files=filedata)

    def Protos(self, request, context):
        paths = ['honeybee.proto']
        return service_pb2.ProtosResponse(file_paths=paths)

    def Examples(self, request, context):
        paths = []
        return service_pb2.ExamplesResponse(file_paths=paths)

    def Tests(self, request, context):
        paths = []
        return service_pb2.TestsResponse(file_paths=paths)

    def Guides(self, request, context):
        paths = []
        return service_pb2.GuidesResponse(file_paths=paths)

    def Status(self, request, context):
        return service_pb2.StatusResponse(status=0)

    def ReservationAdded(self, request, context):
        return service_pb2.ReservationAddedResponse(status=0)

    def ReservationReleased(self, request, context):
        return service_pb2.ReservationReleasedResponse(status=0)


