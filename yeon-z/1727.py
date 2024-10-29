# 커플 만들기
from sys import stdin
N, M = map(int, stdin.readline().split())
MAX = float('inf')

man = sorted(list(map(int, stdin.readline().split())))
woman = sorted(list(map(int, stdin.readline().split())))

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i == j:
            dp[i][j] = dp[i-1][j-1] + abs(man[i-1] - woman[j-1])
        elif i < j:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + abs(man[i-1] - woman[j-1]))
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + abs(man[i-1] - woman[j-1]))

print(dp[-1][-1])