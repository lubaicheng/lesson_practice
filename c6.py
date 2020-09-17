#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :c6.py
@说明    :
@时间    :2020/09/16 23:00:16
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''

import re 
a = 'p1ytho0python1pythonn2'
r = re.findall('ython*',a)
print(r)