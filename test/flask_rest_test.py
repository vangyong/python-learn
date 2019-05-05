#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 说明： flask提供rest接口

from flask import Flask, abort, request, jsonify

app = Flask(__name__)

# 测试数据暂时存放
tasks = []


@app.route('/task', methods=['POST'])
def add_task():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    tasks.append(task)
    return jsonify({'result': 'success'})


@app.route('/task', methods=['PUT'])
def edit_task():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    for t in tasks:
        if int(t['id']) == task['id']:
            t['info'] = task['info']
            return jsonify({'result': 'edit success'})
    tasks.append(task)
    return jsonify({'result': 'add success'})


@app.route('/task/<id>', methods=['GET'])
def get_task(id):
    print(type(id))
    if not id:
        return jsonify({'result': 'id is none'})
    else:
        for t in tasks:
            if int(id) == t['id']:
                return jsonify(t)
        return jsonify({'result': 'not found'})


@app.route('/task/list', methods=['GET'])
def get_task_list():
    return jsonify(tasks)


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=8383, debug=True)
