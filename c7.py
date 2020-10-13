#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :c7.py
@说明    :
@时间    :2020/09/19 19:50:46
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''

import re 
s = 'ABC3721D86'

def convert(value):
    matched = value.group()
    if int(matched) >=6:
        return '9'
    else:
        return '0'

r = re.sub('\d',convert,s)
print(r)