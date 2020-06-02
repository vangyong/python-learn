#!/usr/bin/python3
import scrapy.cmdline
import requests
from bs4 import BeautifulSoup


class WikidatascrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    desc = scrapy.Field()


def get_urls():
    url = "https://www.apache.org/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    human_list = soup.find(id='projects-list')('li')

    urls = []
    for human in human_list:
        url = human.find('a')['href']
        urls.append(url)

    return urls


# 使用scrapy框架爬取
class BookSpider(scrapy.Spider):
    name = 'wikiScrapy'  # 爬虫名称
    start_urls = get_urls()  # 需要爬取的500个网址

    def parse(self, response):
        item = WikidatascrapyItem()
        # name and description
        item['name'] = response.css('span.wikibase-title-label').xpath('text()').extract_first()
        item['desc'] = response.css('span.wikibase-descriptionview-text').xpath('text()').extract_first()

        yield item


if __name__ == '__main__':
    # 执行该爬虫，并转化为csv文件
    scrapy.cmdline.execute(['scrapy', 'crawl', 'wikiScrapy', '-o', 'wiki.csv', '-t', 'csv'])
