#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :作业1.py
@说明    :
@时间    :2020/11/08 19:17:09
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''

with open (r'C:\Users\陆柏成\Desktop\input.txt','r') as file:
    read = file.read()
    DNA_length = len(read)
newfile = open(r'C:\Users\陆柏成\Desktop\output.txt','a')

    # for line in file:
    #     line_handle = line[14:DNA_length]
    #     print(line_handle)
    #     newfile.write(line_handle)
    #     new_DNA_length = len(line_handle)
    #     print(new_DNA_length)
    # newfile.close()


# if __name__ =="__main__":
#     # print(read)
#     print(read_handle)

