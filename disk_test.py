#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：disk_test.py
import os


def disk_usage(path):
    st = os.statvfs(path)
    free = (st.f_bavail * st.f_frsize)
    print free
    total = (st.f_blocks * st.f_frsize)
    print total
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    print used
    try:
        percent = (float(used) / total) * 100
        print percent
    except ZeroDivisionError:
        percent = 0
    return percent


if __name__ == '__main__':
    disk_usage('/data/clickhouse/data')
