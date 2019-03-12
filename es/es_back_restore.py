#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：es_back_restore.py

import configparser
import requests
import json
import time
import logging

cfg = configparser.ConfigParser()
cfg.read('es.conf')
es_url = cfg.get('db', 'es.url')
es_index_pre = cfg.get('db', 'es.index.pre')
es_backup = cfg.get('db', 'es.backup')


def date_trans(startTime, endTime):
    days = set([])
    tartTimeStr = time.strftime("%Y.%m.%d", time.localtime(startTime))
    endTimeStr = time.strftime("%Y.%m.%d", time.localtime(endTime))
    days.add(tartTimeStr)
    days.add(endTimeStr)
    while startTime < endTime:
        startTime = startTime + 86400
        if (startTime < endTime):
            tartTimeStr = time.strftime("%Y.%m.%d", time.localtime(startTime))
            days.add(tartTimeStr)
    return days


def create_backup(startTime, endTime):
    days = date_trans(startTime, endTime)
    flag = 1
    for d in days:
        index = es_index_pre + d
        r1 = requests.get(es_url + '/_snapshot' + es_backup + '/snapshot_' + d)
        if r1.status_code == 404 and r1.reason == 'Not Found':
            json_data = json.dumps({"indices": index, "ignore_unavailable": "false", "include_global_state": "false"})
            r = requests.put(es_url + '/_snapshot' + es_backup + '/snapshot_' + d, json_data)
            if r.status_code != 200:
                logging.info("backup data failed day of " + d)
                logging.info(r.content)
                flag = 0
        else:
            logging.info("the day of" + d + " data has backed  before")
    return flag


def create_reload(startTime, endTime):
    days = date_trans(startTime, endTime)
    flag = 1
    for d in days:
        index = es_index_pre + d
        r0 = requests.get(es_url + '/_snapshot' + es_backup + '/snapshot_' + d)
        if r0.status_code == 200:
            r1 = requests.get(es_url + '/' + index)
            if r1.status_code == 200:
                r2 = requests.delete(es_url + '/' + index)
                logging.info("delete data day of:" + d)
                logging.info(r2.content)

            r = requests.post(es_url + '/_snapshot' + es_backup + '/snapshot_' + d + '/_restore')
            if r.status_code != 200:
                logging.info("restore data failed day of " + d)
                logging.info(r.content)
                flag = 0
        else:
            logging.info("no backup file day of " + d)
            flag = 0
    return flag


def delete_data(startTime, endTime):
    days = date_trans(startTime, endTime)
    flag = 1
    for d in days:
        index = es_index_pre + d
        r = requests.delete(es_url + '/' + index)
        if r.status_code != 200:
            logging.info("delete data failed day of " + d)
            logging.info(r.content)
            flag = 0
    return flag


# 备份： 开始时间戳，结束时间戳 10位到秒  1：成功 0： 失败
# 回迁： 先把文件放入对应的目录 如:/es_backup 开始时间戳，结束时间戳 1：成功 0： 失败
# 删除： 备份完成后删除备份之前一天的数据 开始时间戳，结束时间戳 1：成功 0： 失败
if __name__ == '__main__':
    # create_backup(1545408000, 1545494400)   # 12-20 --12-21
    create_reload(1577203200, 1577289600)  # 12-22 -- 12-23
# delete_data(1545580800, 1545667200)   # 12-24 -- 12-25
