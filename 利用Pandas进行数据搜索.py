#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :利用Pandas进行数据搜索.py
@说明    :利用Pandas进行数据搜索
@时间    :2020/09/23 15:13:50
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv(
    'https://labfile.oss.aliyuncs.com/courses/1283/telecom_churn.csv')
df['Churn'] = df['Churn'].astype('int64')       #将数据类型转换为int64的数据类型
a = df.head()              #查看前5行数据
b = df.shape            #展示维度，包括行数和列数
c = df.columns             #打印列名
# df.info()                 #查看DataFrame的总体信息。
d = df.describe()
e = df.describe(include=['object','bool'])
f = df['Churn'].value_counts(normalize=True)
g = df.sort_values(by='Total day charge', ascending=False).head()
h = df.sort_values(by=['Churn', 'Total day charge'],
               ascending=[True, False]).head()
i = df['Churn'].mean()      #得到一个单独的列
# print(df['Churn'])
j =df.iloc[0,[0,2,3]]      #通过 loc 方法输出 0 至 5 行、1,3,4列的数据
print(j)