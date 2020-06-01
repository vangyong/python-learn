#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：elasticsearch_demo.py

import csv
from elasticsearch import Elasticsearch
import time
import util
import requests
import logging

elastic_search_url = "http://10.4.4.203:9200/"
elastic_search_client = Elasticsearch(hosts="http://10.4.4.203:9200/", http_auth=('', ''))
elastic_search_backup = "\data\elastic_search_backup"


# 创建索引
def create_index(index_name='new', index_type="ott_date"):
    index_mapping = {
        "mappings": {
            index_type: {
                "properties": {
                    "title": {
                        "type": "text",
                        "index": True,
                    },
                    "date": {
                        "type": "date",
                        "store": True,
                        "format": "yyyy/MM/dd HH:mm:ss||yyyy/MM/dd||epoch_millis"
                    },
                    "keyword": {
                        "type": "keyword",
                        "index": "not_analyzed"
                    },
                    "source": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "link": {
                        "type": "string",
                        "index": "not_analyzed"
                    }
                }
            }
        }
    }
    if elastic_search_client.indices.exists(index=index_name) is not True:
        res = elastic_search_client.indices.create(index=index_name, body=index_mapping)
        print(res)


# 删除索引中的一条
def delete_data(index_name, index_type, id):
    res = elastic_search_client.delete(index=index_name, doc_type=index_type, id=id)
    print(res)


# 用bulk批量插入数据
def bulk_add_data(index_name, index_type):
    list = [
        {"date": "2017/09/13",
         "source": "慧聪网",
         "link": "http://info.broadcast.hc360.com/2017/09/130859749974.shtml",
         "keyword": "电视",
         "title": "付费 电视 行业面临的转型和挑战"
         },
        {"date": "2017/09/13",
         "source": "中国文明网",
         "link": "http://www.wenming.cn/xj_pd/yw/201709/t20170913_4421323.shtml",
         "keyword": "电视",
         "title": "电视 专题片《巡视利剑》广获好评：铁腕反腐凝聚党心民心"
         },
        {"date": "2017/09/13",
         "source": "人民电视",
         "link": "http://tv.people.com.cn/BIG5/n1/2017/0913/c67816-29533981.html",
         "keyword": "电视",
         "title": "中国第21批赴刚果（金）维和部隊启程--人民 电视 --人民网"
         },
        {"date": "2017/09/13",
         "source": "站长之家",
         "link": "http://www.chinaz.com/news/2017/0913/804263.shtml",
         "keyword": "电视",
         "title": "电视 盒子 哪个牌子好？ 吐血奉献三大选购秘笈"
         }
    ]
    actions = []
    i = 1
    for line in list:
        action = {
            "_index": index_name,
            "_type": index_type,
            "_id": i,  # _id 也可以默认生成，不赋值
            "_source": {
                "date": line['date'],
                "source": line['source'].decode('utf8'),
                "link": line['link'],
                "keyword": line['keyword'].decode('utf8'),
                "title": line['title'].decode('utf8')}
        }
        i += 1
        print(action)
        actions.append(action)
    success, _ = elastic_search_client.bulk(actions, index=index_name, raise_on_error=True)
    print('Performed %d actions' % success)


def query_by_scroll():
    query_json = {}
    result = elastic_search_client.search(index='csoc-logs-2018.12.21*', body=query_json, scroll='5m', size=100)

    results = result['hits']['hits']  # es查询结果第一页
    total = result['hits']['total']  # es查询结果总量
    scroll_id = result['_scroll_id']  # 游标用于输出es查询所有结果

    for i in range(0, int(total / 100) + 1):
        # scroll参数必须指定否则会报错
        query_scroll = elastic_search_client.scroll(scroll_id=scroll_id, scroll='5m')['hits']['hits']
        results += query_scroll

    with open('\data\es_back\logs_data-2018.12.21.csv', 'w', newline='', encoding='utf-8') as flow:
        csv_writer = csv.writer(flow)
        for res in results:
            source = res['_source']
            row_data = [res['_id'], source]
            csv_writer.writerow(row_data)


def time_to_days(start_time, end_time):
    days = set([])
    tart_time_str = time.strftime("%Y.%m.%d", time.localtime(start_time))
    end_time_str = time.strftime("%Y.%m.%d", time.localtime(end_time))
    days.add(tart_time_str)
    days.add(end_time_str)
    while start_time < end_time:
        start_time = start_time + 86400
        if (start_time < end_time):
            next_day_str = time.strftime("%Y.%m.%d", time.localtime(start_time))
            days.add(next_day_str)
    return days


def backup_data(index_pre, start_time, end_time):
    days = time_to_days(start_time, end_time)
    flag = 1
    for d in days:
        index = index_pre + d
        r1 = requests.get(elastic_search_url + '/_snapshot' + elastic_search_backup + '/snapshot_' + d)
        if r1.status_code == 404 and r1.reason == 'Not Found':
            json_data = util.dumps({"indices": index, "ignore_unavailable": "false", "include_global_state": "false"})
            r = requests.put(elastic_search_url + '/_snapshot' + elastic_search_backup + '/snapshot_' + d, json_data)
            if r.status_code != 200:
                logging.info("backup data failed day of " + d)
                logging.info(r.content)
                flag = 0
        else:
            logging.info("the day of" + d + " data has backed  before")
    return flag


def reload_data(index_pre, start_time, end_time):
    days = time_to_days(start_time, end_time)
    flag = 1
    for d in days:
        index = index_pre + d
        r0 = requests.get(elastic_search_url + '/_snapshot' + elastic_search_backup + '/snapshot_' + d)
        if r0.status_code == 200:
            r1 = requests.get(elastic_search_url + '/' + index)
            if r1.status_code == 200:
                r11 = requests.delete(elastic_search_url + '/' + index)
                logging.info("delete data day of:" + d)
                logging.info(r11.content)

            r2 = requests.post(
                elastic_search_url + '/_snapshot' + elastic_search_backup + '/snapshot_' + d + '/_restore')
            if r2.status_code != 200:
                logging.info("restore data failed day of " + d)
                logging.info(r2.content)
                flag = 0
        else:
            logging.info("no backup file day of " + d)
            flag = 0
    return flag
