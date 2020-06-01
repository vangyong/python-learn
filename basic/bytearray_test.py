#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc : 常见的序列有：list   tuple  str  bytes(字节串)  bytearray

_a1 = 'a1_value'  # 单下划线 保护变量
__b1 = 'b1_value'  # 私有成员
__sysparam__ = 'sysparam_value'  # 系统定义名字  __init__() 构造函数

b1 = bytearray([1, 2, 3])
print(b1)
print(bytearray(3))
print(bytearray("abc", encoding="utf-8"))

b2 = bytes()
print(b2)
b2 = b'b2222'
print(b2)
b3 = b'hello'
print(b3[0])
b4 = bytes('我爱Python编程', encoding='utf-8')
print(b4)
b5 = "学习Python很有趣".encode('utf-8')
print(b5)
st = b5.decode('utf-8')
print(st)  # 学习Python很有趣
