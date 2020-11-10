#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :作业12.py
@说明    :
文件input.txt包含几个DNA序列，一行一个。每个序列的前14个碱基为应该去除的接头序列(sequencing adapter)。请编写如下要求的程序：
1.	将每个DNA的接头序列去除，并把这些去掉接头的序列写入另一个新文件中
2.	将这些去掉接头的DNA序列的长度分别打印出来


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