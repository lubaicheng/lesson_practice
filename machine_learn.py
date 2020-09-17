#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :c6.py
@说明    :
@时间    :2020/09/16 22:26:21
@作者    :陆柏成
@版本    :1.0
@Email   :lu_baicheng@163.com
'''

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X=iris.data
iris_y=iris.target
X_train,X_test,y_train,y_test=train_test_split(iris_X,iris_y,test_size=0.3)
print(y_train)
