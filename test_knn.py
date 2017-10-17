#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kNN
import numpy as np
group_pre=np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 3, 1]])

print(kNN.classify0(np.array([1, 2, 3.3]), group_pre, ['a', 'c', 'c', 'c'], 2))

