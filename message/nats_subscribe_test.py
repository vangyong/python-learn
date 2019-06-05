#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：nats_subscribe_test.py

import asyncio
from nats.aio.client import Client as NATS


async def run(loop):
    nc = NATS()

    await nc.connect("nats://10.10.19.53:4222", loop=loop)

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))

    await nc.subscribe("subject", cb=message_handler)

    # Gracefully close the connection.
    await nc.drain()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()
