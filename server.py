from concurrent import futures

import datetime

import grpc
import hw_pb2
import hw_pb2_grpc

from google.protobuf import struct_pb2


class Greeter(hw_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hw_pb2.HelloResponse(message=f"Hello, {request.name}")

    def ReturnJson(self, request, context):
        timestamp = request.timestamp
        request_date = datetime.datetime.fromtimestamp(timestamp.seconds).date()
        today = datetime.date.today()

        response = struct_pb2.Struct()

        if request_date == today:
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            response.update(data)

        else:
            response.fields["message"].string_value = f"No data for the requested date: {request_date}. "

        print(response)
        return hw_pb2.JsonMessage(data=response)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    hw_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port(f"[::]:{port}")

    server.start()
    print(f"Server started, listening on {port}")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
