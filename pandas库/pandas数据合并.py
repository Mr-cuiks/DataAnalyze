# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# df1 = pd.DataFrame(np.zeros((2, 5)), index=['A', 'B'], columns=['v', 'w', 'x', 'y', 'z'])
# df2 = pd.DataFrame(np.ones((3, 4)), index=['A', 'B', 'C'])
# print(df1)
# print(df2)
#
# print(df1.join(df2))
# print(df2.join(df1))


# df1 = pd.DataFrame({'姓名': ['张三', '李四', '赵六'], '部门': ['研发部', '财务部', '市场部']})
# df2 = pd.DataFrame({'姓名': ['张三', '李四', '王五'], '专业': ['计算机', '会计', '市场营销']})
# df1.index = [2, 3, 4]
# print(df1)
# # print(df2)
# # print(pd.merge(df1, df2, how='inner', on='姓名'))
# df3 = df1.rename(columns={'姓名': '员工姓名'})
# df4 = df2.rename(columns={'姓名': '学生姓名'})
# df3['地址'] = ['天津', '北京', '上海']
# df4['地址'] = ['天津', '上海', '北京']
# print(df3)
# print(df4)
# print(pd.merge(df3, df4, how='inner', left_on=['员工姓名'], right_on=['学生姓名'], suffixes=('a', 'b')))

# 分组和聚合

df = pd.read_csv('data/2015.csv')


group = df.groupby(by='Region')
print(group.mean())
# for i, j in group:
#     # print('地区：',i,'幸福指数：',j['Happiness Score'].mean())
#     print('地区：', i, '\n', '幸福指数：', np.around(j.iloc[:, 3].mean(), 2), '幸福指数最大值：', np.around(j.iloc[:, 3].max(), 2),
#           '幸福指数最小值：', np.around(j.iloc[:, 3].min(), 2))



# def foo(rank):
#     if rank <= 10:
#         return 1
#     elif rank <= 20:
#         return 2
#     elif rank <= 30:
#         return 3
#     elif rank <= 4:
#         return 4
#     else:
#         return 5
#
#
# df_tmp = df['Happiness Rank'].apply(foo)
# df_new = df
# df_new['rank level'] = df_tmp
# print(df_new.head())
# print(df.head())
