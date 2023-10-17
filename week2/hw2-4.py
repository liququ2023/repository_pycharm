# 笨办法求解根号2(while)
# 输入2可以得到结果
a = int(input())
b = a/2
while True:
    c = (b+a/b)/2
    if abs(b-c) < 0.00001:
        break
    b = c
b = "%f" % b
print(b)
