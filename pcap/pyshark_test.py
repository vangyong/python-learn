#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：pyshark_test.py

import pcap
import json
import logging

# 获取网卡
# cap = pyshark.FileCapture('ens33')
# cap.sniff(timeout=50)

cap = pcap.FileCapture('test.pcap')
print("type of cap:")
print(type(cap))
print(cap)
print('----------------------------------')
print("type of cap[0]:")
print(type(cap[0]))
print(cap[0])
print("type of cap[1]:")
print(type(cap[1]))
print(cap[1])
print('----------------------------------')
print("type of cap[0][0]:")
print(type(cap[0][0]))
print(cap[0][0])
print('----------------------------------')
print("type of cap[0][1]:")
print(type(cap[0][1]))
print(cap[0][1])
print('----------------------------------')
print("type of cap[0][1].layer_name")
print(type(cap[0][1].layer_name))
print(cap[0][1].layer_name)
print('----------------------------------')
print("type of cap[0][1].field_names")
print(type(cap[0][1].field_names))
print(cap[0][1].field_names)
print('----------------------------------')
print("type of cap[0][1].field_names[0]")
print(type(cap[0][1].field_names[0]))
print(cap[0][1].field_names[0])
