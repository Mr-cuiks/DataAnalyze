# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
month_3 = [i for i in range(1, 32)]
month_5 = [i for i in range(51, 82)]
print(month_3)
print(len(month_5))
a = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22,
     23]

b = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12,
     13, 6]
print(len(a))
xtick_lable_3 = ['3月{}日'.format(i) for i in month_3]
xtick_lable_10 = ['10月{}日'.format(i - 50) for i in month_5]

# plt.subplot(211)
# plt.scatter(month, a, label='3月')
# plt.xticks(month[::2], xtick_lable_3[::2], rotation=270)
# plt.subplot(212)
# plt.scatter(month, a, label='10月')
# plt.xticks(month[::2], xtick_lable_10[::2], rotation=270)
# plt.show()
# plt.figure(figsize=(10, 4), dpi=80)
plt.scatter(month_3, a, c='r', label='3月')
plt.scatter(month_5, b, label='5月')
plt.legend(loc='upper left')
month = month_3 + month_5
xtick_lable = xtick_lable_3 + xtick_lable_10
plt.xticks(month[::3], xtick_lable[::3], rotation=90)
plt.show()
