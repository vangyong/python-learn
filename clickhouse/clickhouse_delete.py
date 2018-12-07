#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：clickhouse_delete.py
# 刪除指定天之前的數據

from clickhouse_driver.client import Client
import ConfigParser
import datetime

cfg = ConfigParser.ConfigParser()
cfg.read('clickhouse.conf')
db_url = cfg.get('db','db_url')
db_database = cfg.get('db','db_database')
db_user = cfg.get('db','db_user')
db_pass = cfg.get('db','db_pass')
data_days = cfg.get('data','data_days')
data_tables = cfg.get('data','data_tables').split(',')

before_day = datetime.datetime.now()-datetime.timedelta(days=int(data_days))

client = Client(db_url, database=db_database, user=db_user, password=db_pass)

for t in data_tables:
    format_day = before_day.strftime('%Y-%m-%d')
    sql_str = 'ALTER TABLE '+t+' DROP PARTITION \''+format_day+'\''
    print sql_str
    client.execute(sql_str)
    print '删除表:'+t+' 数据'

