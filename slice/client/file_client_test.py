#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import Ice
import FileServer

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("SimpleFileServer:default -h 127.0.0.1 -p 10030")
    fileserver = FileServer.FileReadServerPrx.checkedCast(base)
    if not fileserver:
        raise RuntimeError("Invalid proxy")
    param_buff = bytes()
    ret_buff = b''
    # fileserver.ReadPcap('1', 0, 10, ret_buff)
    ret_buff = fileserver.ReadPcap('1', 0, 10)
    print(ret_buff)

    # 调试test1方法
    # param1 = 'ppp01'
    # ret_test1 = fileserver.test1(param1)
    # print(ret_test1)
