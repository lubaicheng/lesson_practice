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
a = 'PythonqC#JavaPHPC#'


def convert(value):
    matched = value.group()
    return '!!'+ matched +'!!'

r = re.sub('C#',convert,a)

if __name__ == "__main__":
    print(r)
