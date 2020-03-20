#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import time

# url地址
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
    t1 = time.time()  # 开始时间
    print('#' * 50)

    req = requests.get(base_url, headers=headers)  # 发送HTTP请求
    soup = BeautifulSoup(req.text, "lxml")
    project_list = soup.find(id='projects-list')('li')
    for project in project_list:
        if project.find('a'):
            project_url = project.find('a')['href']
            urls.append(project_url)
    for url in urls:
        parser(url)
    t2 = time.time()  # 结束时间
    print('一般方法，总共耗时：%s' % (t2 - t1))
    print('#' * 50)