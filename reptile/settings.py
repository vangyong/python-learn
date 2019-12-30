#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc :

import scrapy

class WikidatascrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    desc = scrapy.Field()
