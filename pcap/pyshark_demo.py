#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pcap
import json
import pyshark

# 抓取linux网卡
# cap = pyshark.FileCapture('ens33')
# cap.sniff(timeout=50)

# 抓取windows网卡
# tshark_path = 'D:\\Program Files\\Wireshark\\tshark.exe'
# capture = pyshark.LiveCapture(output_file="catch.pcap", interface="本地连接", tshark_path=tshark_path)
# capture.sniff(timeout=10)


fileCapture = pyshark.FileCapture('test.pcap')
packet_list = []
for packet in fileCapture:
    packet_dict = {}
    packet_dict['frame_info'] = packet.frame_info
    layer_list = []
    for layer in packet:
        layer_dict = {}
        layer_dict['layer_name'] = layer.layer_name
        field_list = []
        field_names = layer.field_names
        for field_name in field_names:
            field_dict = {}
            field_dict['field_name'] = field_name
            field_dict['field_value'] = layer.get_field_value(field_name)
            field_list.append(field_dict)
        layer_dict['field_list'] = field_list
        layer_list.append(layer_dict)
    packet_dict['layers'] = layer_list
    packet_list.append(packet_dict)
print(packet_list)
