#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import Ice
import filecenter


class FileServerI(filecenter.FileReader):
    # pcap包下载
    def ReadPcap(self, sfileid, offset, len, current=None):
        # print('get a client request:%s', sfileid)
        # f = open("foo.txt", "rb", True)
        # f.seek(offset)
        # ret_buff = b''
        # ret_buff = f.read(len)
        # # seek_res = f.seek(offset, len)
        # # print('server端读取的字符串seek_res：' + seek_res)
        # print('server端读取的字符串ret：' + ret_buff.decode('utf-8'))
        # return ret_buff

        # 测试返回
        print('get a client request:%s', sfileid)
        ret_buff = b'abcd'
        # print('server端读取的字符串seek_res：' + seek_res)
        print('server端读取的字符串ret：' + ret_buff.decode('utf-8'))
        ret_tuple = (ret_buff,)
        return ret_tuple

    # 测试方法
    def test1(self, fileid, current=None):
        print('get a client request:%s', fileid)
        ret_str = 'this is return string'
        return ret_str


with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("SimpleFilecenterAdapter", "default -h 127.0.0.1 -p 10030")
    object = FileServerI()
    adapter.add(object, communicator.stringToIdentity("SimpleFilecenter"))
    adapter.activate()
    communicator.waitForShutdown()
