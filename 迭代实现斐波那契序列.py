#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :c17.py
@说明    :迭代实现斐波那契序列
@时间    :2020/12/15 15:17:14
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''
def fib(n):
    a,b =1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
    
print(fib(9))

# for i in range(1, 20):
#     print(fib_recur(i), end=' ')



    