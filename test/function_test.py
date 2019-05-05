#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：function_test.py

from functools import reduce

# for a in range(10):
#     print(a)

# print([(lambda x: x * x)(x) for x in range(4, 11)])
# print((lambda x: x * x)(3))

# f = filter(lambda x: x * x - 4, range(3))
# print(next(f))

# f = map(lambda x: x * x - 4, range(10))
# print(next(f))


# print(reduce(lambda x, y: x * y - 4, range(4)))
# print(reduce(lambda x, y: x + y, range(101)))
print(reduce(lambda x, y: x + y, range(101), 100))
