# -*- coding: utf-8 -*-

import SOAPpy

server = SOAPpy.SOAPProxy("http://localhost:8080/")
results = server.hello()
print(results)