#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：clickhouse_demo.py

from clickhouse_driver.client import Client
import pymysql
import logging
import datetime

clickhouse_client = Client('10.4.4.101', database='default', user='default', password='')

mysql_connect = pymysql.connect(host='10.10.143.2', port=3306, user='root', password='root', db='microservice_system',
                                charset="utf8")
mysql_cursor = mysql_connect.cursor()


# 创建表
def create_table():
    clickhouse_client.execute('SHOW TABLES')
    clickhouse_client.execute('DROP TABLE IF EXISTS test')
    clickhouse_client.execute('CREATE TABLE test (x Int32) ENGINE = Memory')


# 新增数据
def add_data():
    clickhouse_client.execute(
        'INSERT INTO test (x) VALUES', [{'x': 1}, {'x': 2}, {'x': 3}, {'x': 100}]
    )
    clickhouse_client.execute('INSERT INTO test (x) VALUES', [[200]])


# 查询数据
def query_data():
    print(clickhouse_client.execute('SELECT sum(x) FROM test'))


# 删除数据
def delete_data(database, table, before_day):
    format_day = before_day.strftime('%Y-%m-%d')
    sql_partition = 'SELECT distinct`partition` from system.parts where database=\'' + database + '\' and `table` =\'' + table + '\''
    partitions = clickhouse_client.execute(sql_partition)
    for partition in partitions:
        trimed_partition = str(partition[0]).replace('\'', '').replace('-', '')
        int_partition = int(trimed_partition)
        day_int = int(format_day.replace('\'', '').replace('-', ''))
        if (int_partition <= day_int):
            sql = 'ALTER TABLE ' + table + ' DROP PARTITION ' + partition[0] + ''
            logging.info(sql)
            clickhouse_client.execute(sql)
            logging.info('删除表:' + table + ' 数据分区:' + str(partition[0]))


# 从mysql导入数据
def import_from_mysql():
    mysql_cursor.execute("select * from sys_user ")
    user_data = []
    read_csv = mysql_cursor.fetchall()
    read_csv = list(read_csv)
    for row in read_csv:
        row = list(row)
        user_data.append(row)

    try:
        clickhouse_client.execute('INSERT INTO test  VALUES', user_data, types_check=True)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    create_table();
    before_day = datetime.datetime.now() - datetime.timedelta(days=7)
    delete_data('mytest', 'sys_user', before_day)
