# -*- coding: utf-8 -*-

import SOAPpy


def say_hello():
    return "say hello"


def hello(name, times):
    results = []
    for i in range(0, times):
        results.append('Hello, %s' % name)
    return results


server = SOAPpy.SOAPServer(("localhost", 8080))

server.registerFunction(say_hello)
server.serve_forever()
