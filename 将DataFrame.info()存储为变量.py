#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :c12.py
@说明    :将DataFrame.info()存储为变量
@时间    :2020/09/23 14:17:29
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''

import pandas as pd
 
# 构建数据集
int_values = [1, 2, 3, 4, 5] # 整数
text_values = ['alpha', 'beta', 'gamma', 'delta', 'epsilon'] # 字符串
float_values = [0.0, 0.25, 0.5, 0.75, 1.0] # 浮点
df = pd.DataFrame({"int_col": int_values, "text_col": text_values, "float_col": float_values})
 
# 存储为字符串
import io
buf = io.StringIO() # 创建一个StringIO，便于后续在内存中写入str
df.info(buf=buf) # 写入
s = buf.getvalue() # 读取
print (s,type(s))