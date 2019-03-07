#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：es_test.py

import configparser
import csv
import time
import os
import requests
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers

cfg = configparser.ConfigParser()
cfg.read('es.conf')
es_url = cfg.get('db', 'es.url')
es_index_pre = cfg.get('db', 'es.index.pre')
es_type = cfg.get('db', 'es.type')
es_backup = cfg.get('db', 'es.backup')
es_reload = cfg.get('db', 'es.reload')

es = Elasticsearch(hosts=es_url, http_auth=('', ''))
query_json = {
}


class exportEsData():

    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime

    def exportData(self):
        days = self.dateTrans(self.startTime, self.endTime)
        for d in days:
            query = es.search(index=es_index_pre + d + '*', body=query_json, scroll='5m', size=100)
            if (query['hits']['total'] == 0):
                print(" no data queryed :%s" % d)
            else:
                results = query['hits']['hits']  # es查询出的结果第一页
                total = query['hits']['total']  # es查询出的结果总量
                scroll_id = query['_scroll_id']  # 游标用于输出es查询出的所有结果

                for i in range(0, int(total / 100) + 1):
                    # scroll参数必须指定否则会报错
                    query_scroll = es.scroll(scroll_id=scroll_id, scroll='5m')['hits']['hits']
                    results += query_scroll

                with open(es_backup + es_index_pre + d + '.csv', 'w', newline='', encoding='utf-8') as flow:
                    csv_writer = csv.writer(flow)
                    for res in results:
                        # print(res)
                        # csv_writer.writerow([res['_id'] + ',' + res['_source']])
                        source = res['_source']
                        row_data = [res['_id'], source]
                        csv_writer.writerow(row_data)

    def dateTrans(self, startTime, endTime):
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


class importEsData():

    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime

    def importEsData(self):
        days = self.dateTrans(self.startTime, self.endTime)
        for d in days:
            if (os.path.exists(es_reload + es_index_pre + d + '.csv')):
                csv_file = csv.reader(open(es_reload + es_index_pre + d + '.csv', 'r', encoding='UTF8'))
                actions = []
                for row in csv_file:
                    id = row[0]
                    source = row[1]
                    action = {
                        "_index": es_index_pre + d,
                        "_type": "logs",
                        "_id": id,
                        "_source": eval(source)
                    }
                    actions.append(action)
                helpers.bulk(es, actions)
                del actions[0:len(actions)]
                print("import finish process:%s" % d)
            else:
                print(" no data file day of :%s" % d)

    def dateTrans(self, startTime, endTime):
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


class deleteEsData():

    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime

    def deleteEsData(self):
        days = self.dateTrans(self.startTime, self.endTime)
        for d in days:
            query = json.dumps({
                "query": {"match_all": {}}
            })
            index = es_index_pre + d
            r = requests.post(es_url +'/'+ index + '/logs/_delete_by_query', query)
            print(r.content)

    def dateTrans(self, startTime, endTime):
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


# 导出： 开始时间戳，结束时间戳 10位到秒
# 导入： 先把文件放入对应的目录 如:E:\data\es_reload\ 开始时间戳，结束时间戳
if __name__ == '__main__':
    # exportEsData(1543593600, 1546185600).exportData()
    # importEsData(1543593600, 1546185600).importEsData()
    deleteEsData(1543593600, 1546185600).deleteEsData()
