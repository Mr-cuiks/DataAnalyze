# -*- coding: utf-8 -*-

import numpy as np

t = np.arange(0, 24).reshape(4, 6)
t = t.astype(np.float16)
print(t)
print('*******')
print(t < 10)
# t[t < 10] = 0
# t[t > 10] = 10
t[1, :] = np.nan
print(t)
print('*******')
tt = np.where(t < 10, 0, 10)
tt[np.isnan(t)] = 0
print('空值个数',np.count_nonzero(t != t))
print(tt)
print('*******')
ttt = t.clip(10, 18)
# print(int(np.nan))
print(ttt.sum(axis=0))
