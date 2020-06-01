#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc : hex编码转换

import binascii

if __name__ == '__main__':
    a1_math = binascii.b2a_hex("测试".encode("utf8"))  # b2a_hex 字节转16进制数字
    print(a1_math)

    a1_str = binascii.a2b_hex("e6b58be8af95").decode("utf8")  # a2b_hex 16进制数字转字符串
    print(a1_str)
