#!/usr/bin/env python
# -*- coding: utf-8 -*-

# kNN k阶临近值算法

from numpy import *
import operator
import collections
def createDtaSet():
    group = array([[1., 1.1], [1., 1.], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inx, dataset, labels, k):
    def get_jl(inx, dataset):
        """获取距离"""
        if not isinstance(inx, list):
            return 9, "请确保inx中的数据类型为list类型"
        elif not inx:
            return 1, "没有待计算的数据"
        l = map(lambda x: (x[0]-inx[0])**2+(x[1]-inx[1])**2, dataset)
        return 0, list(l)
    code, len_xy = list(get_jl(inx, dataset))
    if code != 0:
        return code, len_xy
    info_len = []
    # 将距离信息保存为[{索引: 值}], 方便使用list.sort(key=xxx)对其排序
    for i in range(len(len_xy)):
        info_len.append({i:len_xy[i]})
    info_len.sort(key=lambda x: list(x.values())[0], reverse=True)
    aim_labels = list(map(lambda x: list(x.keys())[0], info_len[:k]))
    def count_info(aim_list):
        """对返回的标签信息计数, 以返回最多的标签"""
        return 0, collections.Counter(aim_labels).most_common(1)[0][0]
    aim_labels = list(map(lambda x: labels[x], aim_labels))
    return count_info(aim_labels)

dataset, labels = createDtaSet()
print(classify0([1,1], dataset, labels, 2))


