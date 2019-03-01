#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：clickhouse_delete.py
# 刪除指定天之前的数据

from clickhouse_driver.client import Client
import logging
import configparser
import datetime
import os

cfg = configparser.ConfigParser()
cfg.read('clickhouse.conf')
db_url = cfg.get('db', 'db_url')
db_database = cfg.get('db', 'db_database')
db_user = cfg.get('db', 'db_user')
db_pass = cfg.get('db', 'db_pass')
data_days = int(cfg.get('data', 'data_days'))
data_tables = cfg.get('data', 'data_tables').split(',')

data_content = cfg.get('data', 'data_content')
data_percent = float(cfg.get('data', 'data_percent'))

before_day = datetime.datetime.now() - datetime.timedelta(days=data_days)

client = Client(db_url, database=db_database, user=db_user, password=db_pass)


# 获取磁盘剩余情况
def disk_usage(path):
    st = os.statvfs(path)
    free = (st.f_bavail * st.f_frsize)
    print(free)
    total = (st.f_blocks * st.f_frsize)
    print(total)
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    print(used)
    try:
        percent = (float(used) / total) * 100
        print(percent)
    except ZeroDivisionError:
        percent = 0
    return percent


# 删除数据
def delete_data():
    for t in data_tables:
        format_day = before_day.strftime('%Y-%m-%d')
        sql_partition = 'SELECT distinct`partition` from system.parts where database=\'' + db_database + '\' and `table` =\'' + t + '\''
        partitions = client.execute(sql_partition)
        for p in partitions:
            p_trim = str(p[0]).replace('\'', '').replace('-', '')
            p_int = int(p_trim)
            day_int = int(format_day.replace('\'', '').replace('-', ''))
            if (p_int <= day_int):
                sql_str = 'ALTER TABLE ' + t + ' DROP PARTITION ' + p[0] + ''
                logging.info(sql_str)
                client.execute(sql_str)
                print('删除表:' + t + ' 数据分区:' + str(p[0])) 
                logging.info('删除表:' + t + ' 数据分区:' + str(p[0]))

logging.info('开始执行')
delete_data()
percent = float(disk_usage(data_content))
if (percent < data_percent):
    data_days = data_days - 1
    delete_data()
    logging.info('执行完毕')
