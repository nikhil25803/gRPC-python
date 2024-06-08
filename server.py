from concurrent import futures
import time
import grpc
import greet_pb2
import greet_pb2_grpc


class GreeterService(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        """
        Unary Method
        """
        print("Unary Request Made")
        print("Request:\n", request)
        hello_reply = greet_pb2.HelloReply(message=f"{request.greeting} {request.name}")
        return hello_reply

    def ParrotSaysHello(self, request, context):
        """
        Server Side Streaming
        """
        print("Server Side Stream Request Made")
        print("Request:\n", request)

        for i in range(3):
            hello_reply = greet_pb2.HelloReply(
                message=f"{request.greeting} {request.name} {i+1}"
            )
            yield hello_reply
            time.sleep(2)

    def ChattyClientSaysHello(self, request_iterator, context):
        """
        Client Side Streaming
        """
        print("Client Side Stream Request Made")
        delayed_reply = greet_pb2.DelayedReply()
        for request in request_iterator:
            print("Request Made: ")
            print(request)
            delayed_reply.request.append(request)
        delayed_reply.message = f"You have sent {len(delayed_reply.request)} messages."
        return delayed_reply

    def InteractingHello(self, request_iterator, context):
        """
        Bi-directional Streaming
        """
        return super().InteractingHello(request_iterator, context)


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    print("Server is running on port: 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    server()
