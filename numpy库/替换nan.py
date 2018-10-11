# -*- coding: utf-8 -*-

import numpy as np

t = np.array([[0, 1, 2, 3],
              [1, np.nan, 3, 4],
              [2, np.nan, np.nan, 5],
              [3, 4, 5, np.nan]])
print(t.shape)
col = t.shape[0]
row = t.shape[1]
for i in range(col):
    for j in range(row):
        if np.isnan(t[i, j]):
            t[i, j] = t[:, j][np.isnan(t[:, j]) == False].sum() / np.count_nonzero(t[:, i] == t[:, i])
print(t)
