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
    f_buff = bytes()
    tup1 = ()
    tup1 = fileserver.ReadPcap('1', 0, 10)
    # f_buff = fileserver.ReadPcap('1', 0, 10)
    print(f_buff)
    # param1 = 'ppp01'
    # ret_str = fileserver.test1(param1)
    # print(ret_str)
