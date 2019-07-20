#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import Ice
import FileServer


class FileServerI(FileServer.FileReadServer):
    def ReadPcap(self, sfileid, offset, len, current=None):
        print('get a client request:%s', sfileid)
        f = open("foo.txt", "rb", True)
        f.seek(offset)
        ret = f.read(len)
        # seek_res = f.seek(offset, len)
        # print('server端读取的字符串seek_res：' + seek_res)
        print('server端读取的字符串ret：' + ret.decode('utf-8'))
        return tuple(ret)

    def test1(self, fileid, current=None):
        print('get a client request:%s', fileid)
        ret_str = 'this is return string'
        return ret_str


with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("SimpleFileServerAdapter", "default -h 127.0.0.1 -p 10030")
    object = FileServerI()
    adapter.add(object, communicator.stringToIdentity("SimpleFileServer"))
    adapter.activate()
    communicator.waitForShutdown()
