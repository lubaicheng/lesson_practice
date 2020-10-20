#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :碱基概率.py
@说明    :
@时间    :2020/10/20 13:16:24
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''


DNA = 'ATCGCGCQTAGCATC'
DNA_len = len(DNA)
conding_area = DNA[:7]+DNA[8:]
ratio = (len(conding_area)/len(DNA))
print(conding_area) 
print(str((ratio)*100) + '%')
print(conding_area.upper())
print(DNA[7:8].lower())