#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：clickhouse_import.py

from clickhouse_driver import Client
import types
import time, datetime
from datetime import date
import pymysql
import warnings
import csv

warnings.filterwarnings('ignore')
pos1 = pymysql.connect(host='10.10.143.2', port=3306, user='root', password='root', db='microservice_system',charset="utf8")
pos = pos1.cursor()

client = Client(host='10.4.4.101', database='default', user='default', password='')

x = 1000
while (x <= 1000):
    client.execute('DROP TABLE IF EXISTS test')
    creattable = """CREATE TABLE test (\
                bill_date date,\
                user_id UInt64,\
                credentials_salt String,\
                mobile_number String,\
                nick_name String,\
                password String,\
                user_name String,\
                delete_status UInt8,\
                gender UInt8\
                )ENGINE=MergeTree(bill_date,(user_id,user_name),8192)"""
    data = []
    start = time.time()
    pos.execute("select * from sys_user ")
    end = time.time()
    print(str(x) + '行mysql数据获取时间', end - start)

    readcsv = pos.fetchall()
    readcsv = list(readcsv)
    for row in readcsv:
        row = list(row)
        data.append(row)

    try:
        client.execute(creattable)
        start = time.time()
        client.execute('INSERT INTO test  VALUES', data, types_check=True)
        end = time.time()
        print(str(x) + 'clickhouse插入时间', end - start)
        print('')
    except Exception as e:
        print(e)
    x = x * 2