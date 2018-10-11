# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import string
import matplotlib.pyplot as plt

line = '****************************'
sline = '--------'
# _a = pd.Series([1, 2, 3, 4])
# print(_a)
# a = pd.Series(_a, index=[1, 2, 3, 4, 5])
# print(a)
#
# print(line)
#
# b_dict = {'a': 0, 'b': 1, 'c': 2}
# b = pd.Series(b_dict)
# print(b.index, type(b.index))
# print(b.values, type(b.values))
# print(b.argmax(), b.argmin())
#
# print(line)
#
# c = pd.Series(np.arange(10, 20), index=list(string.ascii_uppercase[0:10]))
# print(c[c > 15])
#
# print(line)

# d = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list(string.ascii_uppercase[:3]),
#                  columns=list(string.ascii_lowercase[-4:]))
# print(d)
# print(d.ndim, d.index, d.columns)
# print(d.head(2))
# print('---------')
# print(d.loc[['A', 'C'], 'w':'z'])
# print('---------')
# print(d.loc['A', ['w', 'x']])
# print('---------')
# print(d.iloc[[1, 2], [1, 2, 3]])


# print(line)
# file_path = 'data/dogNames2.csv'
# e_data = pd.read_csv(file_path, )
# # print(e_data.head())
# # print(e_data.info())
# # print(e_data[e_data['Count_AnimalName'] > 800])
# # print(sline)
# # print(e_data[(e_data['Row_Labels'].str.len() > 4) & (e_data['Count_AnimalName'] > 700)])
# pic_data = e_data[(e_data['Row_Labels'].str.len() > 2) & (e_data['Count_AnimalName'] > 500)]
# print(pic_data)

# plt.figure(figsize=(10,8))
# plt.bar(np.arange(0,len(pic_data['Count_AnimalName'])),pic_data['Count_AnimalName'])
# plt.xticks(np.arange(0,len(pic_data['Count_AnimalName'])),pic_data['Row_Labels'],rotation=270)
# plt.show()

print(line)
file_path = 'data/IMDB-Movie-Data.csv'
movie_data = pd.read_csv(file_path)
print(movie_data.shape)
# print(movie_data['Director'].tolist())
# print(movie_data['Rating'].mean())
# print(len(movie_data['Director'].unique()))
# all_actor = []
# for actor in movie_data['Actors']:
#     all_actor = all_actor + actor.split(',')
# all_actor = list(set(all_actor))
# print(all_actor)
# print(len(all_actor))


# print(movie_data['Runtime (Minutes)'].tolist())
# print(max(movie_data['Runtime (Minutes)']))
# print(min(movie_data['Runtime (Minutes)']))
# bins = (max(movie_data['Runtime (Minutes)']) - min(movie_data['Runtime (Minutes)'])) // 5
# plt.figure(figsize=(10, 8))
# plt.hist(movie_data['Runtime (Minutes)'], bins)
# plt.xticks([min(movie_data['Runtime (Minutes)']) + 5 * i for i in range(bins+1)])
# plt.grid()
# plt.show()


li = [1,2,3]
li.insert(0,4)
print(li)