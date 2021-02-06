#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time: 2020/10/8 12:11 PM
# @Author: wangyong
# @Version: 1.0.0
# @File: jd_monitor_util.py
# @Desc: jd旗舰店检查到货
# @Link: https://blog.csdn.net/cyz52/article/details/104114438

import requests
import time

# 有货通知 收件邮箱
mail = 'vangyong@126.com'
# 商品的url
url = [
    'https://c0.3.cn/stocks?callback=jQuery628332&type=getstocks&skuIds=69480031035%2C69480031036%2C69480031037%2C69480031038%2C69480031039&area=22_1930_49324_0&_=1602130521396',
    'https://c0.3.cn/stock?skuId=34424081673&area=19_1607_3639_0&venderId=656282&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580214678781491106132&ch=1&callback=jQuery7815511',
    'https://c0.3.cn/stock?skuId=14567560031&area=6_318_320_44149&venderId=70651&buyNum=1&choseSuitSkuIds=&cat=9847,13533,13534&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580535906442142991701&ch=1&callback=jQuery660434',
    'https://c0.3.cn/stock?skuId=100011293952&area=19_1607_4773_0&venderId=1000078145&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580214678781491106132&ch=1&callback=jQuery5497502',
    'https://c0.3.cn/stock?skuId=11300307432&area=2_2824_51916_0&venderId=646174&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1580214678781491106132&ch=1&callback=jQuery4188953',
]


def sendMail(url):
    import smtplib
    from email.mime.text import MIMEText
    # email 用于构建邮件内容
    from email.header import Header

    # 用于构建邮件头

    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '382247015@qq.com'
    password = 'ckdqqdqhnrwbbidj'

    # 收信方邮箱
    to_addr = mail

    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(url + ' 有口罩啦', 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('有口罩啦')

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL(host=smtp_server)
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()


flag = 0
while (1):
    try:

        session = requests.Session()
        session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Connection": "keep-alive"
        }
        print('第' + str(flag) + '次 ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        flag += 1
        for i in url:
            # 商品url
            skuidUrl = 'https://item.jd.com/' + i.split('skuIds=')[1].split('&')[0] + '.html'
            response = session.get(i)
            # print('有货啦! 有货啦! 有货啦! ： ' + skuidUrl)
            # sendMail(skuidUrl)
            if (response.text.find('无货') > 0):
                print('无货 ： ' + skuidUrl)
            else:
                print('有货啦! 有货啦! 有货啦! ： ' + skuidUrl)
                sendMail(skuidUrl)

        time.sleep(5)
    except Exception as e:
        import traceback

        print(traceback.format_exc())
        print('异常')
        time.sleep(10)
