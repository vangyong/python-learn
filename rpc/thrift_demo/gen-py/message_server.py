#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc :


from message import MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


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
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.TServerSocket("localhost", "9090")
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("python thrift server start")
    server.serve()
    print("python thrift server exit")
