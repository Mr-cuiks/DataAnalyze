# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv

plt.rcParams['font.sans-serif'] = ['SimHei']

####数据清洗
# file_path = './BeijingPM20100101_20151231.csv'
# data = np.loadtxt(file_path, dtype='str', delimiter=',', skiprows=1)
# pm_data = data[:, [1, 2, 6, 7, 8, 9]]
# # print(pm_data)
# k = 0
# for i, each_data in enumerate(pm_data):
#     # print(i)
#     for j in each_data:
#         if j == 'NA':
#             # print(pm_data[i-k, :])
#             pm_data = np.delete(pm_data, i - k, axis=0)
#             k += 1
#             break
#
# pm_data = pm_data.astype('int')
# print(pm_data)
# np.savetxt('./cleaned_data.csv', pm_data, delimiter=',', fmt='%.0f')


####计算各个污染程度百分比
file_path = './cleaned_data.csv'
data = np.loadtxt(file_path, dtype='int', delimiter=',')
# print(data)
total_hour = len(data)
us_post_heavy_hour = len(data[data[:, 5] > 150])
medium_data = data[75 < data[:, 5]]
us_post_medium_hour = len(medium_data[medium_data[:, 5] <= 150])
light_data = data[35 < data[:, 5]]
us_post_light_hour = len(light_data[light_data[:, 5] <= 75])
us_post_good_hour = len(data[data[:, 5] <= 35])
us_post_heavy_rate = us_post_heavy_hour / total_hour
us_post_medium_rate = us_post_medium_hour / total_hour
us_post_light_rate = us_post_light_hour / total_hour
us_post_good_rate = us_post_good_hour / total_hour
print('PM_US Post重度污染小时百分比：', us_post_heavy_rate)
print('PM_US Post中度污染小时百分比：', us_post_medium_rate)
print('PM_US Post轻度污染小时百分比：', us_post_light_rate)
print('PM_US Post优良空气小时百分比：', us_post_good_rate)
print()

####计算各个月份的平均情况
mean_monthPm = np.array(['month', 'PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan'])
for year in range(2013, 2016):
    print(data)
    year_data = data[data[:, 0] == year]
    months = np.unique(year_data[:, 1])
    for month in months:
        month_data = year_data[year_data[:, 1] == month]
        month_result = np.mean(month_data[:, [2, 3, 4]], axis=0)
        time = str(year) + '-' + str(month)
        result = np.hstack(([time, month_result]))
        mean_monthPm = np.vstack((mean_monthPm, result))
print(mean_monthPm)
with open('month_result.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for each_data in mean_monthPm:
        writer.writerow(list(each_data))

labels = ['重度污染', '中度污染', '轻度污染', '优良空气']
explode = [0.1, 0, 0, 0]
pie_data = [us_post_heavy_hour, us_post_medium_hour, us_post_light_hour, us_post_good_hour]
colors = ['r', 'b', 'y', 'g']
plt.figure(figsize=(5, 5))
plt.pie(pie_data, labels=labels, explode=explode, autopct='%.2f %%', colors=colors)
plt.savefig('./bing.png')
plt.show()
