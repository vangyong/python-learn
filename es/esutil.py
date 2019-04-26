#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：elasticsearch_back_relocation.py

import configparser
import utils
import os
import time
import urllib.request

cfg = configparser.ConfigParser()
cfg.read('es.conf')
es_url = cfg.get('db', 'es.url')
es_index = cfg.get('db', 'es.index')
es_type = cfg.get('db', 'es.type')


class exportEsData():
    size = 10000

    def __init__(self, url, index, type):
        self.url = url + "/" + index + "/" + type + "/_search"
        self.index = index
        self.type = type

    def exportData(self):
        print("export data begin...")
        begin = time.time()
        try:
            os.remove(self.index + "_" + self.type + ".json")
        except:
            os.mknod(self.index + "_" + self.type + ".json")
        msg = urllib.urlopen(self.url).read()
        print(msg)
        obj = utils.loads(msg)
        num = obj["hits"]["total"]
        start = 0
        end = num / self.size + 1
        while (start < end):
            msg = urllib.urlopen(self.url + "?from=" + str(start * self.size) + "&size=" + str(self.size)).read()
            self.writeFile(msg)
            start = start + 1
        print("export data end!!!\n\t total consuming time:" + str(time.time() - begin) + "s")

    def writeFile(self, msg):
        obj = utils.loads(msg)
        vals = obj["hits"]["hits"]
        try:
            f = open(self.index + "_" + self.type + ".json", "a")
            for val in vals:
                a = utils.dumps(val["_source"], ensure_ascii=False)
                f.write(a + "\n")
        finally:
            f.flush()
            f.close()


class importEsData():
    def __init__(self, url, index, type):
        self.url = url + "/" + index + "/" + type
        self.index = index
        self.type = type

    def importData(self):
        print("import data begin...")
        begin = time.time()
        try:
            f = open(self.index + "_" + self.type + ".json", "r")
            for line in f:
                self.post(line)
        finally:
            f.close()
        print("import data end!!!\n\t total consuming time:" + str(time.time() - begin) + "s")

    def post(self, data):
        req = urllib.Request(self.url, data, {"Content-Type": "application/json; charset=UTF-8"})
        urllib.urlopen(req)


if __name__ == '__main__':
    exportEsData("http://10.4.4.203:9200", "csoc-logs-*", "logs").exportData()

    # importEsData("http://10.4.4.203:9200", "csoc-logs-*", "logs").importData()
