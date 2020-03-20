#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/20 14:12
# @Author : wangyong
# @Desc : 编码转换

import re
import binascii


def split1(str):
    t = ''
    for i in range(int(len(str) / 2)):
        t += str[2 * i:2 * (i + 1)] + ' '
    t = t.upper()
    return t


def split2(str):
    t = str.upper()
    p = re.compile('.{1,2}')  # 匹配任意字符1-2次
    return ' '.join(p.findall(t))


def split3(str):
    t = str.upper()
    return ' '.join([t[2 * i:2 * (i + 1)] for i in range(int(len(t) / 2))])


def parse_to_hex(str):
    str_array = str.split()
    ret_str = ''
    for i in range(len(str_array)):
        i_hex = binascii.b2a_hex(str_array[i].encode("utf8"))
        i_str = binascii.a2b_hex(i_hex).decode("utf8")
        ret_str = ret_str + i_str
    return ret_str


if __name__ == '__main__':
    # # 待分割字符串
    # myStr = 'faa5fbb5fcc5fdd5010200000028000001900000000a002d00000000017d7840000003e800005fa55fb55fc55fd5'
    #
    # # 分割后：
    # # FA A5 FB B5 FC C5 FD D5 01 02 00 00 00 28 00 00 01 90 00 00 00 0A 00 2D 00 00 00 00 01 7D 78 40 00 00 03 E8 00 00 5F A5 5F B5 5F C5 5F D5
    #
    # print('原始字符串：\n' + myStr + '\n')
    # str1 = split1(myStr)
    # print('split1符串：\n' + str1 + '\n')
    # str2 = split2(myStr)
    # print('split2字符串：\n' + str2 + '\n')
    # str3 = split3(myStr)
    # print('split3字符串：\n' + str3 + '\n')

    # a1 = 'FA A5 FB B5 FC C5 FD D5 01 02 00 00 00 28 00 00 01 90 00 00 00 0A 00 2D 00 00 00 00 01 7D 78 40 00 00 03 E8 00 00 5F A5 5F B5 5F C5 5F D5'
    # a1_s1 = a1.replace(' ', '')
    # print('replaced符串：\n' + a1_s1 + '\n')
    #
    # a1_bytes = bytes.fromhex(a1_s1)
    # print("a1_bytes:")
    # print(a1_bytes)
    #
    # a1_math = binascii.b2a_hex(a1_s1.encode("utf-8"))
    # print("a1_math:")
    # print(a1_math)
    #
    # a1_hex = a1_bytes.hex()
    # print("a1_hex:")
    # print(a1_hex)

    b1 = 'FA A5 FB B5 FC C5 FD D5 01 02 00 00 00 28 00 00 01 90 00 00 00 0A 00 2D 00 00 00 00 01 7D 78 40 00 00 03 E8 00 00 5F A5 5F B5 5F C5 5F D5'
    b1_str = parse_to_hex(b1)
    print("b1_str:")
    print(b1_str)
