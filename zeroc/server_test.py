#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Ice
import sys
import Demo


class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print('this is server print:')
        print(s)


with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000")
    object = PrinterI()
    adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
    adapter.activate()
    communicator.waitForShutdown()
