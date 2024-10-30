# 소수&팰린드롬
# 에라토스테네스의 체 + 구현
from sys import stdin
n = 2000000
m = int(stdin.readline())
e = [False, False] + [True] * (n-1)


for i in range(2, n + 1):
    if e[i]:
        target = str(i)
        if i >= m and target == target[::-1]:
            print(i)
            break
        for j in range(2 * i, n + 1, i):
            e[j] = False