#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc : 调用参数解析

import argparse
import sys

parse = argparse.ArgumentParser()
parse.add_argument("--learning_rate", type=float, default=0.01, help="initial learning rate")
parse.add_argument("--max_steps", type=int, default=2000, help="max")
parse.add_argument("--hidden1", type=int, default=100, help="hidden1")
arg = parse.parse_args()

print(sys.argv[0:])
print(type(sys.argv[0:]))
print(sys.argv[1:])
print(type(sys.argv[1:]))

print('-------arg:')
print(arg)
print(type(arg))

print('-------vars arg:')
print(vars(arg))  # vars返回对象的属性词典
print(arg.learning_rate)
print(arg.max_steps)
print(arg.hidden1)

# 命令行执行
# python3 argparse_test.py --learning_rate=20 --max_steps=10
# python3 argparse_test.py --learning_rate 20 --max_steps 10
