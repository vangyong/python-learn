#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time: 2021/2/6 4:02 PM
# @Author: wangyong
# @Version: 1.0.0
# @File: datetime_test.py
# @Desc: 时间处理
from datetime import datetime

# 格式化为字符串
now_time = datetime.now()
str_time = datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
print( type(str_time))
print(str_time)

# 格式化为时间对象
obj_time = datetime.strptime('2017-8-1 18:20:20', '%Y-%m-%d %H:%M:%S')
print( type(obj_time))
print(obj_time)