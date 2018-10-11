# -*- coding: utf-8 -*-

import numpy as np

t = np.arange(20).reshape(4,5)
print(t)
t[[1,2],:] = t[[2,1],:]
print(t)