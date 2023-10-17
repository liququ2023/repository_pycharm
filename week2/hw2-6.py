c = float(input('请输入一个实数：'))
def newton_1(m):
    x0 = m
    x1 = x0/2+m/(x0*2)
    while abs(x1-x0) > 1e-5:
        x0 = x1
        x1 = x0 / 2 + m / (x0 * 2)
    return x1
print('%.4f'%newton_1(c))
def newton_4(m):
    x0 = m/4
    x1 = x0/2+m/(x0*2)
    while abs(x1-x0) > 1e-5:
        x0 = x1
        x1 = x0 / 2 + m / (x0 * 2)
    return x1
print('%.4f'%newton_4(c))
