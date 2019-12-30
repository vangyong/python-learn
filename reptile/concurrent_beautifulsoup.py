import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

# 开始时间
t1 = time.time()
print('#' * 50)

url = "http://www.wikidata.org/w/index.php?title=Special:WhatLinksHere/Q5&limit=500&from=0"
# 请求头部
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
# 发送HTTP请求
req = requests.get(url, headers=headers)
# 解析网页
soup = BeautifulSoup(req.text, "lxml")
# 找到name和Description所在的记录
human_list = soup.find(id='mw-whatlinkshere-list')('li')

urls = []
# 获取网址
for human in human_list:
    url = human.find('a')['href']
    urls.append('https://www.wikidata.org'+url)

# 获取每个网页的name和description
def parser(url):
    req = requests.get(url)
    # 利用BeautifulSoup将获取到的文本解析成HTML
    soup = BeautifulSoup(req.text, "lxml")
    # 获取name和description
    name = soup.find('span', class_="wikibase-title-label")
    desc = soup.find('span', class_="wikibase-descriptionview-text")
    if name is not None and desc is not None:
        print('%-40s,\t%s'%(name.text, desc.text))

# 利用并发加速爬取
executor = ThreadPoolExecutor(max_workers=20)
# submit()的参数： 第一个为函数， 之后为该函数的传入参数，允许有多个
future_tasks = [executor.submit(parser, url) for url in urls]
# 等待所有的线程完成，才进入后续的执行
wait(future_tasks, return_when=ALL_COMPLETED)

t2 = time.time() # 结束时间
print('并发方法，总共耗时：%s' % (t2 - t1))
print('#' * 50)