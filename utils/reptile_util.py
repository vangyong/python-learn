#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc : 爬虫工具

import requests
import re
import redis
from pyquery import PyQuery as pq

loginUrl = 'https://manage.xxx.com.cn/home/login'
userName = 'xxx'
passWord = 'xxx'

redisServer = '192.168.0.2'
redisPort = 6379
redisPass = ''

productList = {'椰油': 'CL_Spot', '咖啡': 'COFFEE', '工业铜': 'COPPER'}
volumeList = {'CL_Spot': [0, 0], 'COFFEE': [0, 0], 'COPPER': [0, 0]}


def main():
    jsessionid = getCookie()
    doLogin(jsessionid)
    dataUrl = 'https://manage.xxx.cn/?pageNo=1&pageSize=100'
    cookies = {'JSESSIONID': jsessionid}
    r = requests.get(dataUrl, cookies=cookies)
    dom = pq(r.text)
    lines = dom('table').eq(1).find('tr').items()
    for line in lines:
        line = re.sub(r'<!--.*-->', '', str(line))
        pattern = re.compile(r'<td>(.*?)</td>')
        group = pattern.findall(line)
        if not group:
            continue
        productCode = productList[group[3]]
        if group[6] == '买':
            volumeList[productCode][0] += int(group[7]) * int(group[8])
        if group[6] == '卖':
            volumeList[productCode][1] += int(group[7]) * int(group[8])

    redisClient = redis.Redis(host=redisServer, port=redisPort, password=redisPass)
    for x in volumeList:
        keyUp = 'redis_order_count_u_%s' % x
        keyDown = 'redis_order_count_d_%s' % x
        redisClient.set(keyUp, int(volumeList[x][0]))
        redisClient.set(keyDown, int(volumeList[x][1]))


def getCookie():
    ua = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    r = requests.get(loginUrl, headers=ua)
    return r.cookies['JSESSIONID']


def doLogin(jsessionid):
    param = {'userName': userName, 'password': passWord}
    cookies = {'JSESSIONID': jsessionid}
    requests.post(loginUrl, data=param, cookies=cookies)


if __name__ == '__main__':
    main()