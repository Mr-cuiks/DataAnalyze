# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

file_path = './US_video_data_numbers.csv'

data = np.loadtxt(file_path, delimiter=',', dtype='int')

data = data[data[:,3]<=20000]
click_num = data[:, 3]
print(len(click_num))
print(max(click_num) - min(click_num))
nums = (max(click_num) - min(click_num)) // 1000
print(nums)
plt.hist(click_num, nums)
plt.show()
print(click_num)

# data = data[data[:,1]<=500000]
# like_num = data[:, 1]
# comment_num = data[:, 3]
# plt.figure(figsize=(15, 8), dpi=80)
# plt.xlabel('likes-num')
# plt.ylabel('comment-nums')
# plt.scatter(like_num, comment_num, c='r')
# plt.show()
