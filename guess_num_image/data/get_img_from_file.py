#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import numpy as np
from PIL import Image

"""
    将字符改为图片, 
    将图片改为字符, 采用相反过程
"""
with open("0_0.txt") as f:
    each_line = f.readlines()
    x = [list(map(int, list(x.strip()))) for x in each_line]
    np_int_list = np.array(x)
    # x, y = np_int_list.shape
    np_int_list = np.where(np_int_list == 1, 255, 0)
    print(np_int_list[0])
    im = Image.fromarray(np_int_list)
    im.show()


