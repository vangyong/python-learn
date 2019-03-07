#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：es_back_restore.py

import configparser
import requests
import json

cfg = configparser.ConfigParser()
cfg.read('es.conf')
es_url = cfg.get('db', 'es.url')
es_index_pre = cfg.get('db', 'es.index.pre')
es_type = cfg.get('db', 'es.type')
es_backup = cfg.get('db', 'es.backup')
es_reload = cfg.get('db', 'es.reload')


def create_backup(startTime, endTime):
    data = json.dumps({
        "type": "fs",
        "settings": {
            "location": "/mount/backups/my_backup"
        }
    })
    r = requests.put(es_url+'/_snapshot/my_backup', data)
    print(r.content)
    print("-----------------------")
    print(r.content)


# 导出： 开始时间戳，结束时间戳 10位到秒
# 导入： 先把文件放入对应的目录 如:E:\data\es_reload\ 开始时间戳，结束时间戳
if __name__ == '__main__':
    # exportEsData(1543593600, 1546185600).exportData()
    # importEsData(1543593600, 1546185600).importEsData()
    create_backup(1545321600, 1545321600)
