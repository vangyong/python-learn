#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：datetime-test.py

import datetime
import logging

now_time = datetime.datetime.now()

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    filename='E:\data\logs\python-tool\datetime-test.log', level=logging.WARNING)
logging.debug('debug 信息')
logging.warning('只有这个会输出。。。')
logging.info('info 信息')
logging.info('info 信息' + datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S'))
