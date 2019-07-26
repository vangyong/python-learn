
1、导出依赖包
pip freeze > requirements

2、安装依赖包
pip install -r requirements


ice 生成代码(需先安装ice)
slice2py Printer.ice

protobuf 生成代码（需先安装protoc）
protoc -I=E:\mygit\python-tool\rpc --python_out=E:\mygit\python-tool\rpc E:\mygit\python-tool\rpc\addressbook.proto

https://www.jianshu.com/p/419efe983cb2