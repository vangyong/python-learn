#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：nats_subscribe_test.py

import asyncio
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers


async def run(loop):
    nc = NATS()

    await nc.connect("nats://127.0.0.1:4222", loop=loop)

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))

    # "*" matches any token, at any level of the subject.
    # await nc.subscribe("foo.*.baz", cb=message_handler)
    # await nc.subscribe("foo.bar.*", cb=message_handler)

    # ">" matches any length of the tail of a subject, and can only be the last token
    # E.g. 'foo.>' will match 'foo.bar', 'foo.bar.baz', 'foo.foo.bar.bax.22'
    await nc.subscribe("subject", cb=message_handler)

    # Matches all of the above.
    # await nc.publish("foo.bar.baz", b'Hello World')

    # Gracefully close the connection.
    await nc.drain()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()
