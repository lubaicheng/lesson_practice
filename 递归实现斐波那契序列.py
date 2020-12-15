#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :c18.py
@说明    :递归实现斐波那契序列
@时间    :2020/12/15 15:30:39
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''
def fib(n):
    if(n<=1):
        return n
    return fib(n-1)+fib(n-2)

print(fib(9))
