#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc : 关键字测试

from collections.abc import Iterable

global_v1 = 6


# global变量
def f1():
    global global_v1
    print(global_v1)
    global_v1 = 3


# range函数
def f2():
    for i in range(10):
        print(i)


# Iterable遍历
def f3():
    it = iter([1, 2, 3, 4, 5])
    print(isinstance(it, Iterable))
    while True:
        try:
            x = next(it)
            print(x)
        except StopIteration:
            break


# lambda表达式
def f4():
    print([(lambda x: x * x)(x) for x in range(4, 11)])
    print((lambda x: x * x)(3))


if __name__ == '__main__':
    # f1()
    # print(global_v1)
    f4()
