from datetime import datetime

import grpc
import pytz

from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf import json_format

import hw_pb2
import hw_pb2_grpc


def run():
    port = "50051"

    print("Will try to greet world ...")
    with grpc.insecure_channel(f"localhost:{port}") as channel:
        stub = hw_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hw_pb2.HelloRequest(name="Antohny Montana"))

    print("Greeter client received: " + response.message)

    print("Let's collect some data ...")
    timestamp = Timestamp()
    timezone = pytz.timezone("Europe/Warsaw")
    current_timezone_now = datetime.now(timezone)
    timestamp.FromDatetime(current_timezone_now)

    with grpc.insecure_channel(f"localhost:{port}") as channel:
        stub = hw_pb2_grpc.GreeterStub(channel)
        response = stub.ReturnJson(hw_pb2.JsonRequest(timestamp=timestamp))
        json_str = json_format.MessageToJson(response.data)

    print("Greeter client received JSON: " + json_str)

    if len(json_str) > 12:
        with open('response_data.json', 'w') as json_file:
            json_file.write(json_str)


if __name__ == "__main__":
    run()
