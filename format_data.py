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
            spa_data = list(map(lambda x: [float(y) for y in x[:3]], list_data_list))
            labels = [x[-1] for x in list_data_list]
            np_labels = np.array(labels)
            num_labels = np.where(np_labels == 'didntLike', 0, np.where(np_labels == 'smallDoses', 1, 2))
            code, spa, labels = 0, spa_data, num_labels
        except:
            error = traceback.format_exc()
            code, spa, labels = 9, error, ""
    return code, spa, labels

if __name__ == '__main__':
    tic = time.time()
    print(get_spa_labels())
    toc = time.time()
    print(toc-tic)
