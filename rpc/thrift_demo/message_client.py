#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc :


import thriftpy2
# from thriftpy2.rpc import client_context
from thriftpy2.rpc import make_client

# 读入thrift文件，module_name最好与server端保持一致，也可以不保持一致
message_thrift = thriftpy2.load("message.thrift", module_name="message_thrift")

if __name__ == '__main__':
    client = make_client(message_thrift.MessageService, '127.0.0.1', 9090)
    print(client.ping())

    print(client.sayHello())

    print(client.sendMobileMessage("137",""))