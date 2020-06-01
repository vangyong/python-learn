#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：datetime_test.py

import datetime
import logging
import json


# 类定义
class Man(object):
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 自定义对象转json方法
def obj_2_json(obj):
    return {
        'name': obj.name,
        'age': obj.age
    }


# datetime 时间
def f1():
    now_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    print(now_time)
    print(time_str)


# logging 日志
def f2():
    logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        filename='E:\data\logs\python-tool\datetime-test.log', level=logging.INFO)
    logging.debug('debug 信息')
    logging.warning('只有这个会输出。。。')
    logging.info('info 信息')


def f3():
    p_obj1 = {'name': 'Tom', 'age': 30}
    j_obj1 = json.dumps(p_obj1)
    print(type(j_obj1))
    print(j_obj1)
    print('------man:------')
    m = Man('taaa', 39)
    print(json.dumps(m, default=obj_2_json))

    print('------lambda:------')
    print(json.dumps(m, default=lambda obj: obj.__dict__, sort_keys=True, indent=4))


if __name__ == '__main__':
    f3()
