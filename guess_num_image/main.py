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
