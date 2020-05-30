#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import Ice
import filecenter

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("SimpleFilecenter:default -h 127.0.0.1 -p 10030")
    fileReader = filecenter.FileReaderPrx.checkedCast(base)
    if not fileReader:
        raise RuntimeError("Invalid proxy")
    # param_buff = bytes()
    # ret_buff = b''
    # ret_buff = fileReader.ReadPcap('1', 0, 10)
    # print(ret_buff)

    # 调试test1方法
    param1 = 'ppp01'
    ret_test1 = fileReader.test1(param1)
    print(ret_test1)
