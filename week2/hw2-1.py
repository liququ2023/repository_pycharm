a = []


def f(n):
    q = [1]

    for i in range(1, n + 1):
        q.append(i)
        for j in range(1, i + 1):
            q[i] = max(q[i], (i - j) * q[j])
    return q[n]


n = int(input("请输入一个正整数n："))
result = f(n)
print(result)
