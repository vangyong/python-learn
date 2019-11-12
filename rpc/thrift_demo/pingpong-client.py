#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc :

import thriftpy2
# from thriftpy2.rpc import client_context
from thriftpy2.rpc import make_client

# 读入thrift文件，module_name最好与server端保持一致，也可以不保持一致
pp_thrift = thriftpy2.load("pingpong.thrift", module_name="pp_thrift")


def main():
    # with client_context(pp_thrift.PingService, '127.0.0.1', 6000) as c:
    #    pong = c.ping()
    #    print(pong)
    client = make_client(pp_thrift.PingService, '127.0.0.1', 6000)
    print(client.ping())


if __name__ == '__main__':
    main()
