.PHONY: generate-grpc
generate-grpc:
	- python -m grpc_tools.protoc -I./protos --python_out=./protos --pyi_out=./protos --grpc_python_out=./protos ./protos/greet.proto