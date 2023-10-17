# 牛顿迭代法求立方根

import math
a = float(input('请输入一个实数：'))

def f(x):
    return x**3 - a
def f_derivative(x):
    return 3*x**2

ep = 0.0000001
xk = 1
xk1 = 1

while True:
    xk1 = xk
    xk = xk1-f(xk1)/f_derivative(xk1)
    if math.fabs(xk - xk1) < ep:
        break
print(xk)