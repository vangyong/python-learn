#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：lambda_test.py


import itertools

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)

for n in ns:
    print(n)
