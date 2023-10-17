# 求两个正整数的最大公约数

a = int(input("请输入第一个正整数："))
b = int(input("请输入第二个正整数："))

x = a % b
while x != 0:
    a = b
    b = x
    x = a % b
print(b)
