#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :在指定碱基位置切开两半.py
@说明    :
@时间    :2020/10/20 13:17:45
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''


a = 'ATGCTCGAGAATTCAT'
sum = a.find('GAATTC')
print(a[0:sum+1])
print(a[sum+1:])

    
