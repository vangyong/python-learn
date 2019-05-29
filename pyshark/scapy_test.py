#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：scapy_test.py

from scapy.all import *

cap = rdpcap('test.pcap')
print("type of cap:")
print(type(cap))
print(cap.listname)
res = cap.res
for packet in res:
    a = packet
    print(type(a))
    # print(a.direction)
    # print(a.dst)
    print(a.fields)
    print(a.fields_desc)
    print(a.fieldtype)

print(cap.status)
print(cap)
