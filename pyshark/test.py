#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：pyshark_test.py
#  yum install wireshark 或者 yum install tshark

# import pyshark
import utils

# cap = pyshark.FileCapture('test.pcap')
# print("cap[0]:")
# print(cap[0])
# print("type of cap[0]:")
# print(type(cap[0]))

d = dict(name='Bob', age=20, score=88)
js = utils.dumps(d)
print(js)