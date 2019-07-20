#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc : 包装Decorators


def log(**kw):
    def wrapper(func):
        for k in kw:
            setattr(func, k, kw[k])
        print(getattr(func, 'user', 0))
        print(getattr(func, 'url', 0))
        return func

    return wrapper


@log(user='abc', url='/user/test1')
def now():
    print('2015-3-25')


if __name__ == '__main__':
    now()
