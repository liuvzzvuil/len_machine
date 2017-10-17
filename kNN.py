#!/usr/bin/env python
# -*- coding: utf-8 -*-

# kNN k阶临近值算法

import numpy as np
import operator
import collections
def createDtaSet():
    group = np.array([[1., 1.1], [1., 1.], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inx, dataset, labels, k):
    def get_jl(inx, dataset):
        """获取距离"""
        if not isinstance(inx, np.ndarray):
            return 9, "请确保inx中的数据类型为np.ndarray类型"
        # l = map(lambda x: (x[0]-inx[0])**2+(x[1]-inx[1])**2, dataset)
        l = (dataset - inx) ** 2
        l = l.sum(axis=1)
        # return 0, list(l)
        return 0, l
    code, len_xy = get_jl(inx, dataset)
    if code != 0:
        return code, len_xy

    def get_limit_k():
        info_len = []
        # 将距离信息保存为[{索引: 值}], 方便使用list.sort(key=xxx)对其排序
        for i in range(len(len_xy)):
            info_len.append({i: len_xy[i]})
        # 根据info_len的距离信息对info_len 排序
        info_len.sort(key=lambda x: list(x.values())[0])
        aim_labels = list(map(lambda x: list(x.keys())[0], info_len[:k]))
        return 0, aim_labels
    code, aim_labels_index = get_limit_k()
    if code != 0:
        return code, aim_labels_index

    def count_info(aim_list):
        """对返回的标签信息计数, 以返回最多的标签"""
        return 0, collections.Counter(aim_labels).most_common(1)[0][0]
    aim_labels = list(map(lambda x: labels[x], aim_labels_index))
    return count_info(aim_labels)

def classify1(inx, dataset, labels, k):
    def get_jl(inx, dataset):
        """获取距离"""
        if not isinstance(inx, np.ndarray):
            return 9, "请确保inx中的数据类型为np.ndarray类型"
        # l = map(lambda x: (x[0]-inx[0])**2+(x[1]-inx[1])**2, dataset)
        l = (dataset - inx) ** 2
        l = l.sum(axis=1)
        # return 0, list(l)
        return 0, l
    code, l = get_jl(inx, dataset)
    if code != 0:
        return code, l

    def get_labels(groups):
        """获取前K项的labels"""
        # 获取前K项的最小值
        group_limit_k = np.sort(groups)[-k:]
        min_limit = group_limit_k.min()
        index = np.argwhere(groups >= min_limit)
        index = list(map(lambda x: x[0], index))
        labels_list = []
        for i in index:
            labels_list.append(labels[i])
        return 0, labels_list
    code, aim_labels = get_labels(l)
    if code != 0:
        return code, aim_labels

    def count_info(aim_list):
        """对返回的标签信息计数, 以返回最多的标签"""
        return 0, collections.Counter(aim_list).most_common(1)[0][0]
    # aim_labels = list(map(lambda x: labels[x], aim_labels))
    return count_info(aim_labels)


if __name__ == "__main__":
    dataset, labels = createDtaSet()
    # print(classify1(np.array([1, 1]), dataset, labels, 2))

    # 运行效率测试:
    # import time
    # st = time.time()
    # for _ in range(1000):
    #     classify0(np.array([1, 1]), dataset, labels, 2)
    # et = time.time()
    # print("function 0: ", et-st)
    #
    # st = time.time()
    # for _ in range(1000):
    #     classify1(np.array([1, 1]), dataset, labels, 2)
    # et = time.time()
    # print("function 1: ", et - st)
    # 虽然func1 看起来较整齐并都使用了numpy包, 但是却不如第一个效率高
    print(classify0(np.array([1, 1]), dataset, labels, 2))
