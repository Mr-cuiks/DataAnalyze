# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
df_data = pd.read_csv('data/starbucks_store_worldwide.csv')
s_country = df_data['Country']
print('美国星巴克数量：', s_country.value_counts()['US'])
print('中国星巴克数量：', s_country.value_counts()['CN'])
print()
city_list = []
city_num = []
cn_data = df_data[df_data['Country'] == 'CN']
city_group = cn_data.groupby(by='City')
for city, df_city in city_group:
    city_list.append(city)
    city_num.append(len(df_city))
    print(city, ' 星巴克数量为：', len(df_city))

# 店铺总数前十的国家

country_group = df_data.groupby(by='Country')
country_num = {}
for cou, num in country_group:
    country_num[cou] = len(num)

country_num = sorted(country_num.items(), key=lambda e: e[1], reverse=True)
country_list = [tup[0] for tup in country_num]
store_num = [tup[1] for tup in country_num]
print(country_list[:10])
print(store_num[:10])

plt.bar(range(10), store_num[:10])
plt.xticks(range(10), country_list[:10])
plt.show()

# 中国城市和数量绘图
plt.figure(figsize=(40,20))
plt.bar(range(len(city_list)), city_num)
plt.xticks(range(len(city_list)), city_list,rotation=270)
plt.savefig('城市星巴克数量.png')
plt.show()
