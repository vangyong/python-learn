#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import Ice
import FileServer


class FileServerI(FileServer.FileReadServer):
    def ReadPcap(self, sfileid, offset, len):
        print('get a client request:')
        f = open("foo.txt", "r+")
        str = f.read(offset, len)
        seek_res = f.seek(offset, len)
        print('server端读取的字符串str：' + str)
        print('server端读取的字符串seek_res：' + seek_res)
        return str


with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("SimpleFileServerAdapter", "default -h 127.0.0.1 -p 10030")
    object = FileServerI()
    adapter.add(object, communicator.stringToIdentity("SimpleFileServer"))
    adapter.activate()
    communicator.waitForShutdown()
