#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :test.py
@说明    :
@时间    :2020/09/11 10:19:53
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''

import re 

a = 'C|java|python'

b = re.findall('python',a)
if len(b) > 0:
    print('a中含有python')
else:
    print('No')