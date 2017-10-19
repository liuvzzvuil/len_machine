#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np



def data2array(file_name='0_0.txt'):
    with open(file_name) as f:
        each_line = f.readlines()
        x = [list(map(int, list(x.strip()))) for x in each_line]
        np_int_list = np.array(x)
        np_int_list = np.where(np_int_list == 1, 255, 0)
        np_int_list = np_int_list.reshape(1, -1)[0]
    return np_int_list


def get_spa_labels(test=False):
    labels = []
    spa = []
    if test:
        dir_name = os.path.join("data", "testDigits")
    else:
        dir_name = os.path.join("data", "trainingDigits")
    file_name_list = os.listdir(dir_name)
    for i in file_name_list:
        labels.append(int(i[0]))
        spa.append(data2array(os.path.join(dir_name, i)))

    spa = np.array(spa)
    return spa, labels


if __name__ == '__main__':
    # print(data2array())
    print(get_spa_labels(True))
