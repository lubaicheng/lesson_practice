#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :碱基的配对转换.py
@说明    :
@时间    :2020/10/20 13:18:50
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''


def DNA_CONVERT(sequence):
    sequence = sequence.upper()
    sequence = sequence.replace('A','t')
    sequence = sequence.replace('T','a')
    sequence = sequence.replace('G','c')
    sequence = sequence.replace('C','G')
    return sequence.upper()

def DNA_REVERSE(sequence):
    sequence = sequence.upper()
    return sequence[::-1]

def replace1(self):
    self = self.upper()
    return self

r1 = DNA_CONVERT('AtGCATGCATGC')
r2 = DNA_REVERSE('AtGCATGCATGC')
r3 = replace1('AtGCATGCATGC') 

    

if __name__ == "__main__":
    print(r1,r2)
    print(r3)