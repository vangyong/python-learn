#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from scapy.all import *

pcap = rdpcap('test.pcap')
print("type of cap:", type(pcap))
print(pcap.listname)
res = pcap.res
for packet in res:
    a = packet
    print(type(a))
    print(a.fields)
    print(a.fields_desc)
    print(a.fieldtype)
