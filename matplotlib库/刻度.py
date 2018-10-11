# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random

plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(20, 8))
x = range(120)

y = [random.uniform(20, 35) for i in range(120)]
plt.title('每分钟')

plt.plot(x, y)

_x_ticks = ['10点{}分'.format(i) for i in x if i < 60]
_x_ticks += ['11点{}分'.format(i - 60) for i in x if i > 60]

plt.xticks(x[::5], _x_ticks[::5], rotation=45)
plt.savefig('./fenzhong.png')

plt.show()
