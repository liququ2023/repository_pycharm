# 根据蒙特卡洛法法思想计算定积分
import numpy as np
import math
import matplotlib.pyplot as plt
num = 1000

x = np.arange(2, 3, 1/num * 1)
y = x*x + 4*x*np.sin(x)
plt.plot(x, y)
plt.plot(x, [max(y)]*num, 'r')
plt.plot([max(x)]*num, y, 'r')
plt.plot(x, [0]*num, 'r')
plt.plot([0]*num, y, 'r')


x_list = np.random.random((1, num)) * max(x)
y_list = np.random.random((1, num)) * max(y)


yy_list = 4*x_list*np.sin(x_list)
list = (yy_list-y_list)
n = 0
# print(len(x))
for i in range(len(x)):
    if list[0, i] > 0:
        n += 1
ratio = n/len(x)
area = max(x) * max(y)
value = ratio * area
print(value)

plt.show()