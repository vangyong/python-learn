#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/10/14 14:12
# @Author : wangyong
# @Desc : 文件操作

try:
    fh = open("testfile", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()
