#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：kafka_producer_test.py

import threading, logging, time
import multiprocessing

from kafka import KafkaConsumer, KafkaProducer

BOOTSTRAP_SERVERS = '127.0.0.1:9092'


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)

        while not self.stop_event.is_set():
            producer.send('test1', b"test")
            producer.send('test1', b"\xc2Hola, mundo!")
            time.sleep(1)

        producer.close()


# 读取数据
class Consumer(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS,
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
        # 订阅某个topic
        consumer.subscribe(['test1'])

        while not self.stop_event.is_set():
            for message in consumer:
                print(message)
                if self.stop_event.is_set():
                    break

        consumer.close()


def main():
    tasks = [
        Producer()
       # Consumer()
    ]

    for t in tasks:
        t.start()

    time.sleep(3600)

    for task in tasks:
        task.stop()

    for task in tasks:
        task.join()


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
