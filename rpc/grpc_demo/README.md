
## 环境安装
* pip install grpcio
* pip install grpcio-tools

## 生成代码
* python -m grpc_tools.protoc -I=./ --python_out=./rpc_package --grpc_python_out=./rpc_package ./helloworld.proto

