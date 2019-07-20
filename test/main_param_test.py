#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc : 主函数带参数调用

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world')
    elif len(args) == 2:
        print('Hello %s' % args[1])
    else:
        print
        'Too many arguments!'


if __name__ == '__main__':
    test()
