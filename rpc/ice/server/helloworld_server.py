#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Ice
import sys
import helloworld


class GreeterI(helloworld.Greeter):
    def printString(self, s, current=None):
        print('this is server print:')
        print(s)


with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("SimpleGreeterAdapter", "default -p 10000")
    object = GreeterI()
    adapter.add(object, communicator.stringToIdentity("SimpleGreeter"))
    adapter.activate()
    communicator.waitForShutdown()
