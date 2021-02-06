#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time: 2021/2/6 12:33 PM
# @Author: wangyong
# @Version: 1.0.0
# @File: chromedriver_test.py
# @Desc: chromedriver测试
# @Link https://www.cnblogs.com/jasmine0112/p/12745493.html

from selenium import webdriver
import time

wd = webdriver.Chrome()
wd.get("https://www.baidu.com")    # 打开百度浏览器
wd.find_element_by_id("kw").send_keys("天气")   # 定位输入框并输入搜索词
wd.find_element_by_id("su").click()   #点击[百度一下]按钮进行搜索
time.sleep(3)   #等待3秒
wd.quit()   #关闭浏览器