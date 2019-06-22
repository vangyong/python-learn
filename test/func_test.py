#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：func_test.py


# 可变参数函数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
#
# calc_res = calc(1, 2)
# print(calc_res)
#
# l1 = [1, 2, 3]
#
# calc_l1 = calc(*l1)
# print(calc_l1)

# 关键字参数函数
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
#
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, **extra)


# 命名关键字参数
# def person(name, age, *, city, job):
#     print(name, age, city, job)
#
#
# person('Jack', 24, city='Beijing', job='Engineer')


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1, 2, 3, 'a', 'b', x=99)
