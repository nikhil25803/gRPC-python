import time
import grpc
import greet_pb2
import greet_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)

    print(
        """-- Welcome to gRPC application ---
          1. SayHello - Unary Call
          2. ParrotSaysHello - Server Side Streaming
          3. ChattySaysHello - Client Side Streaming
          4. InteractingHello - Binary Streaming      
        """
    )

    rpc_call = input("Which RPC would you like to call: ")

    if rpc_call == "1":
        hello_request = greet_pb2.HelloRequest(greeting="Namaste!", name="gRPC")
        hello_reply = stub.SayHello(hello_request)
        print("Unary Call SayHello Responded: \n", hello_reply)

    elif rpc_call == "2":
        print("Server Side Streaming")
    elif rpc_call == "3":
        print("Client Side Streaming")
    elif rpc_call == "4":
        print("Binary Streaming")
    else:
        print("Invalid Option")
        return False


if __name__ == "__main__":
    while True:
        run()
