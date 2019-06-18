#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

import FileServer
import Ice


class FileServerI(FileServer.Printer):
    def printString(self, s, current=None):
        print(s)


with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000")
    object = FileServerI()
    adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
    adapter.activate()
    communicator.waitForShutdown()
