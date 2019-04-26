#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：json_test.py

import json


class Man(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def obj_2_json(obj):
    return {
        'name': obj.name,
        'age': obj.age
    }


if __name__ == '__main__':
    p_obj1 = {'name': 'Tom', 'age': 30}
    j_obj1 = json.dumps(p_obj1)
    print('type of j_obj1')
    print(type(j_obj1))
    print(j_obj1)
    print('------man------')
    m = Man('taaa', 39)
    print(json.dumps(m, default=obj_2_json))

    print('------lambda------')
    print(json.dumps(m, default=lambda obj: obj.__dict__, sort_keys=True, indent=4))
