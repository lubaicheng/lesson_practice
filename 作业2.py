#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :作业2.py
@说明    :文件genomic_dna.txt包含基因组DNA的一部分，文件exons.txt包含DNA中多个外显子的开始-结束位置（中间用逗号分隔），一行标注一个。请编写程序将各个外显子抽提出来，并连接成一个完整的编码序列，最后输出到一个文件中

提示：这里可能需要int（）这个函数，它能将数字字符串转换为真正的数字，如：int（‘456’）=456

@时间    :2020/11/10 15:27:59
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''
file1 = open (r'C:\Users\陆柏成\Desktop\genomic_dna.txt') 

file2 = open (r'C:\Users\陆柏成\Desktop\exons.txt')

filenew = open (r'C:\Users\陆柏成\Desktop\tt.txt','w')


DNA_new = file1.read().rstrip()

conding = ''

for line in file2:

    list_exons = line.rstrip().split(',')
    start = int(list_exons[0]) - 1
    end = int(list_exons[1])
    conding += DNA_new[start:end]
    filenew.write(conding)
    print(list_exons)
filenew.close()
file1.close()
file2.close()
