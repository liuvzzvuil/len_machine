#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import numpy as np
import traceback

def get_spa_labels(path=""):
    """ 返回特征值和数字化的标签 0 dislike 1, little, 2 ok"""
    if not path:
        path = "data/kNndata1.txt"
    with open(path) as f:
        try:
            each_line = f.readlines()
            list_data_list = [x.split() for x in each_line]
            spa_data = np.array(list(map(lambda x: [float(y) for y in x[:3]], list_data_list)))
            labels = [x[-1] for x in list_data_list]
            # np_labels = np.array(labels)
            # num_labels = np.where(np_labels == 'didntLike', 0, np.where(np_labels == 'smallDoses', 1, 2))
            # 在只有1000行的情况下, 下述方法较快, 或许当数据量增大的时候会是第一个快些
            num_labels = np.array([1 if x == 'didntLike' else 2 if x == 'smallDoses' else 3 for x in labels])
            code, spa, labels = 0, spa_data, num_labels
        except:
            error = traceback.format_exc()
            code, spa, labels = 9, error, ""
    return code, spa, labels

def auto_norm(data_set):
    """将数据归一化"""
    """目前的数据格式为[[1,2,3], [2, 3,4]]"""
    assert isinstance(data_set, np.ndarray), "数据类型必须为numpy.ndarray"
    min = data_set.T.min(1)
    max = data_set.T.max(1)
    new_col = (data_set - min)/(max-min)
    return new_col, min, (max-min)

if __name__ == '__main__':
    tic = time.time()
    code, spa, labels = get_spa_labels()
    # test = np.array([[1., 2., 3.], [3., 4., 2.], [2., 3., 1.], [4., 3., 2.]])
    print(auto_norm(spa))
    toc = time.time()
    print(toc-tic)
