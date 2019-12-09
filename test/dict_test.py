#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/10/14 14:12
# @Author : wangyong
# @Desc : 字典操作

dict = {"a": "apple", "b": "banana", "o": "orange"}

print "##########dict######################"
for i in dict:
    print "dict[%s]=" % i, dict[i]

print "###########items#####################"
for (k, v) in dict.items():
    print "dict[%s]=" % k, v

print "###########iteritems#################"
for k, v in dict.iteritems():
    print "dict[%s]=" % k, v

print "###########iterkeys,itervalues#######"
for k, v in zip(dict.iterkeys(), dict.itervalues()):
    print "dict[%s]=" % k, v