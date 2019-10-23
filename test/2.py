#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/21 14:18
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 2.py


with open('test.txt', 'r') as f:
    lines = f.readlines()

# print(lines)
for line in lines:
    # print(line[:-1])
    k = line[:-1]
    print('item["{}"] = {}'.format(k, k))
