#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc :


# import sys
# sys.path.append('./gen-py/parse')

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from message import MessageService

if __name__ == '__main__':
    try:
        transport = TSocket.TSocket('localhost', 9090)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        messageService = MessageService.Client(protocol)
        transport.open()
        messageService.ping()
        mobile_message = "this is client mobile message"
        # messageService.sendMobileMessage(bytes("137", encoding="utf-8"), bytes(mobile_message, encoding="utf-8"))
        # res_mobile = messageService.sendMobileMessage("137", mobile_message)
        # print(res_mobile)
        email_message = "this is client email message"
        # messageService.sendMobileMessage('vangyong@126.com', 'this is client email message')
        print('message send finished!')
    except Thrift.TException as e:
        print('exception')
        print(e)
