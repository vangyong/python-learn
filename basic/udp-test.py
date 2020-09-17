# -*- coding: UTF-8 -*-
import sys
# sys.path.append("/opt/local/lib/python2.7/site-packages/")
# sys.path.append("/usr/local/ssdb/api/python/")
# sys.path.append("/opt/local/lib/python2.7/site-packages/")
import os

from socket import *
from time import ctime

import traceback
import time

host = "192.168.1.1"
port = 514
send_ticket = 10000 * 10000

addr = (host, port)

file_list = []

send_over_ticket = 0


def read_syslogmutline(file_dir):
    global file_list
    file_list = []
    print(file_dir)
    try:
        fobj = open(file_dir, "r")
        line_str = ""
        while True:
            line = fobj.readline()
            if not line:
                break
            # line ="<6>"+line
            line_str = line_str + line
            print(line_str)
            if len(line) < 5 and line.startswith("}"):
                file_list.append(line_str)
                line_str = ""

        fobj.close()
    except:
        print(traceback.format_exc())

    return file_list


# head="SyslogActor"
def read_syslog(file_dir):
    global file_list
    file_list = []
    try:
        fobj = open(file_dir, "r")
        while True:
            line = fobj.readline()
            if not line:
                break
            file_list.append(line)
        fobj.close()
    except:
        print(traceback.format_exc())
    return file_list


udp_socket = socket(AF_INET, SOCK_DGRAM)

if False:
    print(sys.argv[1], sys.argv[2])
    file_list = read_syslog(sys.argv[1])
    # file_list = read_syslog("./all/APT.log")
    # file_list = read_syslog("./all/qiming_fw.log")
    # file_list = read_syslog("./all/qiming_waf.log")
    # file_list = read_syslogmutline("./all/qimingblj.log")
    # file_list = read_syslog("./all/swad_apt.log")

    b_time = time.time()
    total_len = 0.0
    number = 0
    while (send_ticket > 0 and number < int(sys.argv[2])):
        send_ticket = send_ticket - 1
        number = number + 1
        print
        number
        for it in file_list:
            k_r = udp_socket.sendto(it, addr)
            send_over_ticket = send_over_ticket + 1
            total_len = total_len + k_r
            if 0 == (send_ticket % 1):
                use_time = time.time() - b_time
                # print (int)(total_len/use_time/1024/1024)                
                print
                it, "\n"
            if 0 == (send_over_ticket % 10000):
                print
                time.time(), send_over_ticket
        if number >= int(sys.argv[2]):
            break

else:
    while True:
        all_file = os.listdir("./all")
        for it in all_file:
            send_ticket = 10000 * 10000
            read_syslog("./all/" + it)
            b_time = time.time()
            total_len = 0.0
            for it in file_list:
                k_r = udp_socket.sendto(it, addr)
                s_len = len(it)
                # print k_r, s_len
                send_ticket = send_ticket - 1
                total_len = total_len + k_r
                if 0 == (send_ticket % 10000):
                    use_time = time.time() - b_time
                    print((int)(total_len / use_time / 1024 / 1024))
                    # print it,"\n"

udp_socket.close()
