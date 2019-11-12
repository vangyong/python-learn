#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc :


import thriftpy2
from thriftpy2.rpc import make_server

message_thrift = thriftpy2.load("message.thrift", module_name="message_thrift")


class MessageServiceHandler:
    def ping(self):
        print("ping")

    def sayHello(self):
        print("sayHello")
        return "sayHello return"

    def sendMobileMessage(self, mobile, message):
        print(mobile)
        print(message)
        print("sendMobileMessage")
        return True

    def sendEmailMessage(self, email, message):
        print(email)
        print("sendEmailMessage")
        return True


if __name__ == '__main__':
    # 定义监听的端口和服务
    server = make_server(message_thrift.MessageService, MessageServiceHandler(), '127.0.0.1', 9090)
    print("serving...")
    server.serve()
    print("python thrift server exit")
