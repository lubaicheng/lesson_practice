#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :c9.py
@说明    :python和json的交互
@时间    :2020/09/20 14:52:40
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''
import json

json_str = '[{"name":"qiyue","age":18},{"name":"qiyue","age":18}]'

student = json.loads(json_str)
student_type = type(student)
print(student,student_type,student[1])