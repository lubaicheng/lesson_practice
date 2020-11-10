#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :c16.py
@说明    :
@时间    :2020/11/10 14:04:53
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''

file2 = open (r'C:\Users\陆柏成\Desktop\exons.txt')

for line in file2:

    list_exons = line.strip().split(',')
    print(list_exons)