#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：datetime_test.py

import datetime
import logging

a = '20180101'
print(a)

now_time = datetime.datetime.now()
time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
print(now_time)
print(time_str)
