# gRPC Implementation in Python

A demo gRPC-based client-server application showcasing different types of gRPC calls.

## What is gRPC?

gRPC is an open-source framework created by Google for remote procedure calls (RPC). It uses the HTTP/2 protocol to send messages in binary format. These messages are serialized and deserialized using Protocol Buffers to define data structures and services.

## Types of gRPC Calls

![image](https://github.com/nikhil25803/gRPC-python/assets/93156825/ec831a07-c5c7-418f-abf6-987475669a0d)


1. **Unary**

   - The client sends a single request to the server and receives a single response.

2. **Server Streaming**

   - The client sends a single request to the server and receives a stream of responses. The server sends multiple responses and finishes with a status message once all responses are sent.

3. **Client Streaming**

   - The client sends a stream of requests to the server. Once the client has finished sending messages, the server processes these requests and sends back a single response.

4. **Bi-Directional Streaming**

   - Both the client and server send streams of messages to each other. This happens parallel, meaning messages can be sent and received in any order.

---
