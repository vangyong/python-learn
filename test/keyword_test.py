#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：keyword_test.py

import datetime
import logging

global_v1 = 6


def f():
    global global_v1
    print(global_v1)
    global_v1 = 3


f()
print(global_v1)
