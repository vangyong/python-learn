#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

import datetime
import logging

a = '20180101'
print a

now_time = datetime.datetime.now()
time_str = datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M:%S')
print now_time
print time_str

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',filename='/logs/test.log', level=logging.DEBUG)
logging.debug('debug 信息')
logging.warning('只有这个会输出。。。')
logging.info('info 信息')
logging.info('info 信息'+datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M:%S'))