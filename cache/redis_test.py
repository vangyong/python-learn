#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
import json

# r = redis.Redis(host='127.0.0.1', port=6379, db=0)
# r.set('name', 'zhangsan')  # 添加
# print(r.get('name'))  # 获取

pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.Redis(connection_pool=pool)
# r.set('test1', 'zhangsantest1')  # 添加
# print(r.get('test1'))  # 获取


user = r.get('cn.segema.learn.springboot1.repository.UserRepository.findById1')
type_user = type(user)
user_json = json.loads(user)
type_user = type(user_json)
user0 = user_json[0]
user1 = user_json[1]
print(user1['userId'])
print('success!')

users = r.get('cn.segema.learn.springboot1.repository.UserRepository.findById1')
type_users = type(users)
users_json = json.loads(users)
type_users = type(users_json)
users0 = users_json[0]
users1 = users_json[1]
print('success!')
