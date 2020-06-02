#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

base_url = "https://www.apache.org/"
# 请求头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}

urls = []


# 解析每个网页
def parser(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    navbar = soup.find('a', class_="navbar-brand")
    if navbar is not None:
        print('navbar %s', navbar)
    if soup.find('img'):
        img_url = soup.find('img')['src']
        print('image url: %s', img_url)


if __name__ == '__main__':
    start_time = time.time()  # 开始时间
    print('#' * 50)
    req = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    project_list = soup.find(id='projects-list')('li')
    for project in project_list:
        if project.find('a'):
            url = project.find('a')['href']
            urls.append(url)

    # 利用并发加速爬取
    executor = ThreadPoolExecutor(max_workers=20)
    # submit()的参数： 第一个为函数， 之后为该函数的传入参数，允许有多个
    future_tasks = [executor.submit(parser, url) for url in urls]

    # 等待所有的线程完成，才进入后续的执行
    wait(future_tasks, return_when=ALL_COMPLETED)

    end_time = time.time()  # 结束时间
    print('并发方法，总共耗时：%s' % (end_time - start_time))
    print('#' * 50)
