# -*- coding: utf-8 -*-

import subprocess
from sys import argv

# 从命令行获取参数
method = argv[1]

# tomcat名，对应路径中tomcat
tomcats = ['tomcat-8.5.31_1', 'tomcat-8.5.31_2','tomcat-8.5.31_3']

if method == "start":
    for tomcat in tomcats:
        res = subprocess.Popen("ps -ef | grep %s | grep -v grep | awk '{print $2}'" % tomcat.split('-', 1)[1], stdout=subprocess.PIPE, shell=True)
        toms = res.stdout.readlines()
        if len(toms) >= 1:
            print u"%s tomcat进程已启动！, pid为：%s\n" % (tomcat, toms[0])
            continue
        print subprocess.Popen('/home/yuwei/%s/bin/startup.sh' % tomcat, stdout=subprocess.PIPE,shell=True).communicate()
        print '\n'
        res = subprocess.Popen("ps -ef | grep %s | grep -v grep | awk '{print $2}'" % tomcat.split('-', 1)[1], stdout=subprocess.PIPE, shell=True)
        toms = res.stdout.readlines()
        if len(toms) == 0:
            print u"%s 启动失败，请检查后重试！\n" % tomcat
        elif len(toms) > 0:
            print u"%s 启动成功， pid为：%s\n" % (tomcat, toms[0])


elif method == "shutdown":
    for tomcat in tomcats:
        res = subprocess.Popen("ps -ef | grep %s | grep -v grep | awk '{print $2}'" % tomcat.split('-', 1)[1], stdout=subprocess.PIPE, shell=True)
        toms = res.stdout.readlines()
        if len(toms) < 1:
            print u"%s tomcat进程未启动！\n" % tomcat
            continue
        print u'正在关闭pid为的%s进程%s\n' % (toms[0], tomcat)
        print subprocess.Popen('/home/yuwei/%s/bin/shutdown.sh' % tomcat, stdout=subprocess.PIPE, shell=True).communicate()
        print '\n'
        res = subprocess.Popen("ps -ef | grep %s | grep -v grep | awk '{print $2}'" % tomcat.split('-', 1)[1], stdout=subprocess.PIPE, shell=True)
        toms = res.stdout.readlines()
        if len(toms) > 0:
            print u"tomcat关闭失败，正在强制关闭\n"
            re = subprocess.Popen("kill -9 %s" % str(toms[0]), shell=True, stdout=subprocess.PIPE)
            print re.stdout.read()


else:
    print u"命令参数错误\n"

