import time
import grpc
import greet_pb2
import greet_pb2_grpc


def get_client_requests_stream():
    """
    Function that yeild different requests because multiple requests are to be made
    to the server before the client gets final response from the sever.
    """
    while True:
        name = input("Please enter a name (leave blank to stop chat): ")

        if name == "":
            break

        hello_request = greet_pb2.HelloRequest(greeting="Hello", name=name)
        yield hello_request
        time.sleep(1)


def run():

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
        print("Unary Call Made.\nSayHello Responded: \n", hello_reply)

    elif rpc_call == "2":
        hello_request = greet_pb2.HelloRequest(greeting="Namaste!", name="gRPC")
        hello_replies = stub.ParrotSaysHello(hello_request)
        for hello_reply in hello_replies:
            print("Server Side Stream Response  Received: ")
            print(hello_reply)

    elif rpc_call == "3":
        delayed_reply = stub.ChattyClientSaysHello(get_client_requests_stream())
        print("Client Side Stream Response Received: ")
        print(delayed_reply)

    elif rpc_call == "4":
        print("Binary Streaming")
    else:
        print("Invalid Option")
        return False


if __name__ == "__main__":
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        while True:
            run()
