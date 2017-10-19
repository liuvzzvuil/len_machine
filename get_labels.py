# -*- coding: utf-8 -*-

import numpy as np

groups = [1, 2, 2, 3]
labels = ['a', 'a', 'b', 'b']

def get_labels(groups, labels, k):
    """获取前K项的labels"""
    # 获取前K项的最小值
    group_limit_k = np.sort(groups)[-k:]
    min_limit = group_limit_k.min()
    index = np.argwhere(groups >= min_limit)
    index = list(map(lambda x: x[0], index))
    labels_list = []
    for i in index:
        labels_list.append(labels[i])
    return labels_list


print(get_labels(groups, labels, 3))

