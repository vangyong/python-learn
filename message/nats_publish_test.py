#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：nats_publish_test.py

import asyncio
import nats.aio.client
import nats.aio.errors


async def send_message(loop):
    mq_url = "nats://10.10.19.53:4222"
    client = nats.aio.client.Client()
    await client.connect(io_loop=loop, servers=[mq_url])
    await client.publish("subject", "this is my python message 中文消息".encode())
    await client.close()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message(loop))
    loop.close()


if __name__ == '__main__':
    main()
