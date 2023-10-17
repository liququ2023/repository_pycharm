# 牛顿法求二次根号

c = float(input('请输入一个实数：'))
def newton(m):
    x0 = m/2
    x1 = x0/2+m/(x0*2)
    while abs(x1-x0) > 1e-5:
        x0 = x1
        x1 = x0 / 2 + m / (x0 * 2)
    return x1
print('%.4f'%newton(c))
