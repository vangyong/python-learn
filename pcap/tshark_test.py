#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py
#  yum install wireshark 或者 yum install tshark
# pip install flask

import pcap
import json

from flask import Flask, abort, request, jsonify

fileCapture = pcap.FileCapture('test.pcap')
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
