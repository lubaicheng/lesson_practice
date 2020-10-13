#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :c13.py
@说明    :
@时间    :2020/09/23 19:07:10
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''

from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK =3 
    RED = 4

r = VIP.YELLOW

if __name__ == "__main__":
    print(r)
