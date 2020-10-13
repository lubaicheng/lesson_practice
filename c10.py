#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :c10.py
@说明    :
@时间    :2020/09/22 19:49:34
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''

import json

student = [
    {'name': 'qiyue','age':18,'flag':False},
    {'name': 'qiyue','age':18}
          ]
json_str=json.dumps(student)
print(json_str,type(json_str))
