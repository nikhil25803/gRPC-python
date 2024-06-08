# gRPC Implementation in Python

A demo gRPC based client-server application with implementation of different types of gRPC calls.

## gRPC?

gRPC is a Google-created, open source, schema-first **Remote Procedure Call** framework that takes advantage of the _HTTP/2_ protocol to transport messages in binary. These messages are serialized and deserialized using Protocol Buffers, which are a type of **Interface Definition Language (IDL).**

## Different types of gRPC calls.

1. **Unary**
   - The client initiates the remote procedure call with the method name, metadata, and the request message. Then the server returns the response with the gRPC status, the response message, and metadata
2. **Server Streaming**
   - The client initiates the remote procedure call with the method name, metadata, and the request message. Then it receives a streaming response from the server. The request’s status is sent to the client at the end of the streaming response (all data has been transmitted to the client along with its metadata)
3. Client Streaming
4. Bi-Directional Streaming
