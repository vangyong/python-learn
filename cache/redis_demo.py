#!/usr/bin/python3
# -*- coding:utf-8 -*-

import redis
import json

# r = redis.Redis(host='127.0.0.1', port=6379,password='123456', db=0)

# 连接池方式
pool = redis.ConnectionPool(host='localhost', port=6379, password='123456', db=0)
db = redis.Redis(connection_pool=pool)

# 字符串 set、get、decr、incr、mget
db.set('str_key', 'zhangsan');
print(db.get('str_key'));

# 哈希 hget、hset、hgetall
db.hset('hash_key', 'name', 'zhangsan');
db.hset('hash_key', 'age', 20);
db.hset('hash_key', 'sex', 'man');
print(db.hget('hash_key', 'sex'));
print(db.hgetall('hash_key'));

# 列表 lpush、rpush、lpop、rpop、lrange
db.lpush('list_key', 'lpush_value1');
db.lpush('list_key', 'lpush_value2');
db.lpush('list_key', 'lpush_value3');
db.rpush('list_key', 'rpush_value1');
db.rpush('list_key', 'rpush_value2');
print(db.lpop('list_key'));
print(db.rpop('list_key'));
print(db.lrange('list_key', 0, 3));

# 集合 sadd、spop、smembers、sunion
db.sadd('set_key', 'set_value1');
db.sadd('set_key', 'set_value2');
print(db.spop('set_key'));
print(db.smembers('set_key'));

# 有序集合 zadd、zrange、zrem、zcard
db.sadd('zset_key', 'zset_value1', 10);
db.sadd('zset_key', 'zset_value2', 20);
db.sadd('zset_key', 'zset_value3', 30);
print(db.zrange('zset_key', 0, -1));
# db.zrem('set_key', 'zset_value2');
# print(db.zcard('set_key'));

# jpa对象数据
# user = r.get('cn.segema.learn.springboot1.repository.UserRepository.findById1')
# type_user = type(user)
# user_json = json.loads(user)
# type_user = type(user_json)
# user0 = user_json[0]
# user1 = user_json[1]
# print(user1['userId'])
# print('success!')
