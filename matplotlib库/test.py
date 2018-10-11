# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import random

x = range(2, 25, 2)

y = []
for i in range(12):
    y.append(random.randint(-10, 10))

print([i for i in x])
print(y)
print(len(y), len(x))
plt.figure(figsize=(20, 8), dpi=80)
plt.title('一天气温变换曲线')
plt.xlabel('时间/h')
plt.ylabel('温度/℃')

# plt.axis([0,24,-10,10])
plt.xticks(x)
plt.plot(x, y)
plt.savefig('./fig_size.png')
plt.show()
