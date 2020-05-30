#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Ice
import sys

import helloworld

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("SimpleGreeter:default -p 10000")
    printer = helloworld.GreeterPrx.checkedCast(base)
    if not printer:
        raise RuntimeError("Invalid proxy")
    print('this is client print:')
    printer.printString("Hello World! This is Client's Message")
    print('client call filished :')
