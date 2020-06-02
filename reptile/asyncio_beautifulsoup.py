#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import time
import aiohttp
import asyncio

# pip3 install aiohttp==1.3.3

base_url = "https://www.apache.org/"
# 请求头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}

urls = []


# 异步HTTP请求
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


# 解析网页
async def parser(html):
    soup = BeautifulSoup(html, "lxml")
    navbar = soup.find('a', class_="navbar-brand")
    if navbar is not None:
        print('navbar %s', navbar)
    if soup.find('img'):
        img_url = soup.find('img')['src']
        print('image url: %s', img_url)


# 处理网页，获取name和description
async def download(url):
    async with aiohttp.ClientSession() as session:
        try:
            html = await fetch(session, url)
            await parser(html)
        except Exception as err:
            print(err)


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

    # 利用asyncio模块进行异步IO处理
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(download(url)) for url in urls]
    tasks = asyncio.gather(*tasks)
    loop.run_until_complete(tasks)

    end_time = time.time()  # 结束时间
    print('使用异步，总共耗时：%s' % (end_time - start_time))
    print('#' * 50)
