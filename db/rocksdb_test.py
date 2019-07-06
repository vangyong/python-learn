#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：rocksdb_test.py

import rocksdb

db = rocksdb.DB("test.db", rocksdb.Options(create_if_missing=True))
db.put(b"a", b"b")
print(db.get(b"a"))
