#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :作业12.py
@说明    :
@时间    :2020/11/08 20:45:15
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''


file = open(r'C:\Users\陆柏成\Desktop\input.txt')
output = open(r'C:\Users\陆柏成\Desktop\output.txt','w')

for dna in file:
    trimmed_dna = dna[14:] #接头序列长度为14
    trimmed_length = len(trimmed_dna) - 1
    output.write(trimmed_dna)

    print('去掉接头后每一个序列长度分别为' + str(trimmed_length))