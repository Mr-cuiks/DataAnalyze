# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


def load_data(rows=[]):
    '''
    在文件中读取数据，并处理'NA'值为'np.nan'。
    :param rows:
    :return:
    '''

    file_path = 'data/BeijingPM20100101_20151231.csv'
    all_data = pd.read_csv(file_path)
    use_data = all_data[rows]
    # 在文件中读取'rows'这几列的数据
    use_data = use_data.dropna()
    # 删除文件中有'NaN'的行
    return use_data


def month_mean(data=pd.DataFrame):
    '''
    获取各个地区每一年每个月份的平均值。
    :return:
    '''
    mean_data = []
    # 创建一个数组用于存放所有的数据
    for year in data['year'].unique():
        # 读取所有的'年份'条目，并去重，即[2013,2014,2015]，然后遍历
        year_data = data[data['year'] == year]
        # 读出当前年份的所有数据
        for month in year_data['month'].unique():
            # 读出当前年份包含的所有月份并去重，然后遍历
            month_data = year_data[year_data['month'] == month]
            # 读出当前月份的所有数据
            result = list(month_data.iloc[:, 2:].mean())
            # 对月份的2，3，4列数据求均值，转化为列表
            result.insert(0, str(year) + '-' + str(month))
            # 在列表第一位插入日期
            mean_data.append(result)
            # 插入当前月份数据到总列表中

    return mean_data


def draw(data=pd.DataFrame):
    '''
    传入一个DataFrame,然后把北京和美国测量数据画图对比
    :param data:
    :return:
    '''

    x_key = list(range(len(data['time'])))
    # 获取time列的长度作为横坐标
    plt.plot(x_key, data['bj'], label='bj_data')
    # 画图
    plt.plot(x_key, data['us'], label='us_data')
    # 画图
    plt.legend(loc='best')
    plt.show()


def main():
    '''
    主函数
    读取文件---获取中美检测数据---计算月度平均---画图比较
    :return:
    '''

    use_data = load_data(['year', 'month', 'PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post'])
    # 获取几列的数据
    month_mean_data = month_mean(use_data)
    # 清洗数据，获取有效值
    bj_us = []
    for row in month_mean_data:
        temp = []
        temp.append(row[0])
        temp.append((row[1] + row[2] + row[3]) / 3)
        temp.append(row[4])
        bj_us.append(temp)
        # 通过循环，往数组中加入所有[时间，北京地区平均值，美国给的数据]
    bj_us = pd.DataFrame(bj_us, columns=['time', 'bj', 'us'])
    # 转化为DataFrame方便操作
    print(bj_us)
    draw(bj_us)


if __name__ == '__main__':
    main()
