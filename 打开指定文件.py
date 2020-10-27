#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :2020.10.20.py
@说明    :
@时间    :2020/10/20 13:55:43
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''


# f = open (r'C:\Users\陆柏成\Desktop\test.txt','r
# ')
with open (r'C:\Users\陆柏成\Desktop\test.txt','r') as file :
    data=file.read()
    t1 = type(data)
    data_delete = data.strip()
    data_delete6 = data.rstrip('6')
    
    

if __name__ == "__main__":
    print(data) 
    print(t1)   
    print('删除空行及换行符号：' + data_delete)
    print('删除末尾数字6：'+ data_delete6)
    

