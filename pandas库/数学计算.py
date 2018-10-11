# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# SUM

# df = pd.DataFrame([[1, 2, 3], [4, 5,6], [7, 8, 9]], index=['A', 'B', 'C'], columns=['c1', 'c2', 'c3'])
# print(df3)
# print(df3.sum())
# print(df3.sum(axis=1))
# print(df3['c1'].sort_values(ascending=False))

# RENAME

# df.index = ['a','b','c']
# df = df.rename(index={'A':'a'})
# print(df.index)

# MERGE
'''
   data1 key  data2
0      1   x      4
1      2   y      5
2      3   z      3
'''
# df1 = pd.DataFrame({'key':['x','y','z'],'data1':[1,2,3]})
# df2 = pd.DataFrame({'key':['x','y','z'],'data2':[4,5,3]})
# print(pd.merge(df1,df2))

# CONCATENATE
# np.concatenate([arr1,arr2],axis=1/0)
# arr1 = np.array(np.arange(0,9).reshape(3,3))
# print(arr1)
# arr2 = np.array(np.arange(0,9).reshape(3,3))
# print(arr2)
#
# print(np.concatenate([arr1,arr2],axis=1))

# CONCAT
# pd.concat([df1,df2])

# df1 = pd.DataFrame(np.arange(9).reshape(3, 3), columns=['A', 'B', 'C'])
# df2 = pd.DataFrame(np.arange(9).reshape(3, 3), columns=['A', 'B', 'D'])
# print(df1)
# print(df2)
# print(pd.concat([df1, df2],axis=1))

# COMBIN_FIRST
# s1.combine_first(s2)
# s1 = pd.Series([1,2,np.nan,4,np.nan],index=['a','b','c','b','e'])
# s2 = pd.Series([1,2,111,4,222],index=['a','b','c','b','e'])
# print(s1.combine_first(s2))


# APPLY

# data = pd.read_csv('data/apply_demo.csv')

# data['A'] = pd.Series(['a']*data.size)
# data['A'] = data['A'].apply(str.upper)

#
# def foo(line):
#     item = line.strip().split(' ')
#     return pd.Series([item[1], item[3], item[5]])
#
# df_tmp = data['data'].apply(foo)
# df_tmp = df_tmp.rename(columns = {0: 'Symbol', 1: 'Seqno', 2: 'Price'})
# data_new = data.combine_first(df_tmp)
# del data_new['data']
# data_new.to_csv('apply_new.csv')
# print(data_new.head())

# 去重

# df = pd.read_csv('data/apply_new.csv')
# del df['Unnamed: 0']
# print(df.size)
# print(len(df))
# # print(df['Seqno'].unique())
# # print(df['Seqno'].duplicated())
# print(df['Seqno'].drop_duplicates().head())
# df_new = df.drop_duplicates(['Seqno'])
# print(df_new.head())

# 时间序列

