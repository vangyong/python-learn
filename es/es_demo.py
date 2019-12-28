#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：es_test.py

import csv
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts="http://10.4.4.203:9200/", http_auth=('', ''))
# print(es.info())

query_json = {
}

query = es.search(index='csoc-logs-2018.12.21*', body=query_json, scroll='5m', size=100)

results = query['hits']['hits']  # es查询出的结果第一页
total = query['hits']['total']  # es查询出的结果总量
scroll_id = query['_scroll_id']  # 游标用于输出es查询出的所有结果

for i in range(0, int(total / 100) + 1):
    # scroll参数必须指定否则会报错
    query_scroll = es.scroll(scroll_id=scroll_id, scroll='5m')['hits']['hits']
    results += query_scroll

with open('E:\data\es_back\logs_data-2018.12.21.csv', 'w', newline='', encoding='utf-8') as flow:
    csv_writer = csv.writer(flow)
    for res in results:
        # print(res)
        # csv_writer.writerow([res['_id'] + ',' + res['_source']])
        source = res['_source']
        row_data = [res['_id'], source]
        csv_writer.writerow(row_data)

print('done!')
# print(es.info())
