#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import format_data
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
code, spa, labels = format_data.get_spa_labels()
# spa = np.array(spa)
x = spa[:,0]
y = spa[:,1]
ax.scatter(x, y, 15 * np.array(labels), 15 * np.array(labels))
ax.set_xlabel("fly")
ax.set_ylabel("冰淇淋消耗数")
plt.show()
