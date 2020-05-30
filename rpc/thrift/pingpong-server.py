#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc :


import thriftpy2
from thriftpy2.rpc import make_server

pp_thrift = thriftpy2.load("pingpong.thrift", module_name="pp_thrift")


# 实现.thrift文件定义的接口
class Dispatcher(object):
    def ping(self):
        print("ping pong!")
        return 'pong'


def main():
    # 定义监听的端口和服务
    server = make_server(pp_thrift.PingService, Dispatcher(), '127.0.0.1', 6000)
    print("serving...")
    server.serve()


if __name__ == '__main__':
    main()
