a = input('请输入一个数组；').split(' ')
a = [int(x) for x in a]
b = [0 for i in range(len(a))]

for i in range(len(a)):
    b[i] = 1
    for j in range(len(a)):
        if i != j:
            b[i] = b[i] * a[i]

print(b)
