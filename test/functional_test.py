#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc : 函数式编程


from functools import reduce

# lambda表达式
# print([(lambda x: x * x)(x) for x in range(4, 11)])
# print((lambda x: x * x)(3))

# f = filter(lambda x: x * x - 4, range(3))
# print(next(f))

# print(reduce(lambda x, y: x * y - 4, range(4)))
# print(reduce(lambda x, y: x + y, range(101)))
# print(reduce(lambda x, y: x + y, range(101), 100))
