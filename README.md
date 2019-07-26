
## 环境安装
    1.导出依赖包
    pip freeze > requirements

    2.安装依赖包
    pip install -r requirements

## ICE 服务
    ice 生成代码(需先安装ice)
    slice2py Printer.ice

## protobuf服务
    protobuf 生成代码（需先安装protoc）
    protoc -I=E:\mygit\python-tool\rpc --python_out=E:\mygit\python-tool\rpc E:\mygit\python-tool\rpc\addressbook.proto

    [引用](https://www.jianshu.com/p/419efe983cb2)
    
## PCAP包解析    