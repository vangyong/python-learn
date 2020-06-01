#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc : 文件操作

import struct


# 大文件复制
def copyFile(f1, f2):
    fs1 = open(f1, 'r')
    fs2 = open(f2, 'w')
    cont1 = fs1.readline()
    while len(cont1) > 0:
        fs2.write(cont1)
        cont1 = fs1.readline()
    fs1.close()
    fs2.close()


def read_bigFile(name):
    f = open(name, 'r')
    cont = f.read(10)
    while len(cont) > 0:
        print(cont)
        cont = f.read(10)
    f.close()


def struct_test():
    # 整型数转字符流
    buf1 = 256
    bin_buf1 = struct.pack('i', buf1)  # 'i'代表'integer'
    print(bin_buf1)
    ret1 = struct.unpack('i', bin_buf1)
    print(ret1)

    # 浮点数转字符流
    buf2 = 3.1415
    bin_buf2 = struct.pack('d', buf2)  # 'd'代表'double'
    print(bin_buf2)
    ret2 = struct.unpack('d', bin_buf2)
    print(ret2)


if __name__ == '__main__':
    f1 = 'E:\\test\\test1.cpp'
    f2 = 'E:\\test_down\\test1.cpp'
    # copyFile(f1, f2)
    # read_bigFile(f1)
    struct_test()
