# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

age = [i for i in range(11, 31)]
print(age)
a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
b = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(len(a))

# plt.subplot(n11) 图表占图形的 1/n
plt.text(20, 4, 'line a')
plt.plot(age, a, label='line a')
plt.text(24, 1, 'line b')
line, = plt.plot(age, b, '-.', label='line b')
# line.set_antialiased(False)
plt.legend(loc='best')
plt.xticks(age)
plt.grid(alpha=0.5)
plt.show()
