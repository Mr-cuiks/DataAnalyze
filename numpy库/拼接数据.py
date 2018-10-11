# -*- coding: utf-8 -*-

import numpy as np

# t1 = np.array([[1,2,3],[2,3,4]])
# t2 = np.array([[1,2,3],[2,3,4]])
#
# print(np.vstack((t1,t2)))
# print(np.hstack((t1,t2)))

us_path = './US_video_data_numbers.csv'
uk_path = './GB_video_data_numbers.csv'

us_data = np.loadtxt(us_path,delimiter=',', dtype='int')
uk_data = np.loadtxt(uk_path,delimiter=',', dtype='int')

us_nums = us_data.shape[0]
uk_nums = uk_data.shape[0]

us_add = np.zeros((us_nums,1),dtype='int')
uk_add = np.ones((uk_nums,1),dtype='int')

us_data = np.hstack((us_data,us_add))
uk_data = np.hstack((uk_data,uk_add))

all_data = np.vstack((us_data,uk_data))
print(all_data)

