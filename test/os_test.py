#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/10/14 14:12
# @Author : wangyong
# @Desc : 系统库操作

import logging
import os
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(filename)s - %(levelname)s - line %(lineno)d - %(message)s',
    filename='/data/logs/dataclean/dataclean.stdout.log')
logger = logging.getLogger(__name__)


class Monitor:
    def __init__(self):
        self.data_days = 7
        self.pcap_path = '/data/storage/pcap'

    def delete_pcap(self):
        time_in_secs = time.time() - (self.data_days * 24 * 60 * 60)
        for root, dirs, files in os.walk(self.pcap_path):
            logger.info(root)
            logger.info(dirs)
            logger.info(files)
            for f in files:
                if f == "CUR_INDEX":
                    continue;

                full_path = os.path.join(root, f)
                stat = os.stat(full_path)

                if stat.st_mtime <= time_in_secs:
                    os.remove(full_path)


if __name__ == '__main__':
    monitor = Monitor()
    logger.info('开始执行')
    monitor.delete_pcap()
