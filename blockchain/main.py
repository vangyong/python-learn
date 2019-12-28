#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   : 2019/12/20 14:12
# @Author : wangyong
# @Desc : 主函数带参数调用

import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import Flask


class Blockchain(object):


app = Flask(__name__)
node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new Block"


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
