#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：iter_test.py

from collections.abc import Iterable

print(isinstance([], Iterable))

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
