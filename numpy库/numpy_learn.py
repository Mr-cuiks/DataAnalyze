# -*- coding: utf-8 -*-

import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)

b = np.array(range(1, 6))
print(b)

c = np.array(np.arange(0.1, 0.6, 0.1))
print(c)

d = np.array([1, 0, 1, 0], dtype=np.bool)
print(d)
print(d.astype(np.int8))

e = np.array([0.100, 0.105])
f = round(8.005, 2)
print(f)

aa = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
print(aa)
print(aa.shape)
print(aa.reshape(4, 3))
print(aa.reshape(2, 2, 3))
print(aa.flatten())

bb = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
print(aa + bb)

cc = np.array([[1], [2], [3]])
print(aa * cc)

print('--------------')
cc = np.array([[1, 2, 3, 4],
               [2, 3, 4, 5]])
print(np.sum(cc, axis=1))

print('********')
dd = np.zeros((3,4),dtype='int')
print(dd)
print('--------')
ee = np.ones((4,5),dtype='int')
print(ee)
print('-*-*-*-*-*-*-*-')
ff = np.eye(5,dtype='int')
print(ff)
print('-*-*-*-*-*-*-*-')
print(aa)
print(np.argmax(aa,axis=0))

