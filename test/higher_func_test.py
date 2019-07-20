#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：higher_func_test.py

from functools import reduce


# map 函数
# l1 = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(l1)


# reduce 函数
# def fn(x, y):
#     return x * 10 + y
#
#
# r1 = reduce(fn, [1, 3, 5, 7, 9])
# print(r1)

# map reduce 实例
# def fn(x, y):
#     return x * 10 + y
#
#
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
#
#
# r2 = reduce(fn, map(char2num, '13579'))
# print(r2)


# 函数作为返回值
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#
#     return sum
#
#
# f = lazy_sum(1, 3, 5, 7, 9)
#
# f()


# 函数包装Decorators
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


now()
