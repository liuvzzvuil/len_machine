#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../kNN')
sys.path.append('data')
import kNN
import get_data
from functools import partial
import numpy as np

def self_test():
    spa, labels = get_data.get_spa_labels()
    spa_test, labels_test = get_data.get_spa_labels(True)
    return spa, labels, spa_test, labels_test


if __name__ == "__main__":
    # print(kNN.test(*self_test()))
    spa, labels = get_data.get_spa_labels()
    test_spa = get_data.data2array('test.txt')
    # nn = list(np.array(test_spa).reshape(-1, 32))
    # print(nn)
    print(kNN.classify0(test_spa, spa, labels, 5))

    # 使用sklearn 包计算
    from sklearn import neighbors
    klt = neighbors.KNeighborsClassifier(n_neighbors=10)
    # print(spa)
    # 训练
    klt.fit(spa, labels)
    test_spa = np.array([test_spa])
    # print(test_spa)
    # 猜测为多少
    pro = klt.predict(test_spa)
    print(pro)
    # guess = klt.predict_proba([[1, 0, 1, 1, 1]])
    # 猜测是这一点的概率为多少
    # print(guess)
    # 详情: http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier
    # http://cwiki.apachecn.org/pages/viewpage.action?pageId=10814109
