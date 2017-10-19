#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random
with open("kNndata1.txt")as f:
    choice_percent = 0.1
    each_lines = f.readlines()
    np_each_lines = np.array(each_lines)
    choice_num = int(len(each_lines) * choice_percent)
    index_list = [x for x in range(len(each_lines))]
    choice_list = random.sample(index_list, choice_num)
    remove_list = list(set(index_list) - set(choice_list))
    np_choiced = np_each_lines[choice_list]
    np_removed = np_each_lines[remove_list]
    choiced = "".join(np_choiced)
    removed = "".join(np_removed)
    with open('test_data.txt', 'w') as f:
        f.write(choiced)
    with open('spa_data.txt', 'w') as f:
        f.write(removed)
