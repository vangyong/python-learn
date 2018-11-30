#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：clickhouse_test.py

from clickhouse_driver.client import Client
import types
import time, datetime
from datetime import date

client = Client('10.4.4.101', database='default', user='default', password='')

client.execute('SHOW TABLES')

client.execute('DROP TABLE IF EXISTS test')

client.execute('CREATE TABLE test (x Int32) ENGINE = Memory')

client.execute(
    'INSERT INTO test (x) VALUES',
    [{'x': 1}, {'x': 2}, {'x': 3}, {'x': 100}]
)
client.execute('INSERT INTO test (x) VALUES', [[200]])

print(client.execute('SELECT sum(x) FROM test'))
