# 1,2,3 더하기 4
from sys import stdin

def solution(n):
    dp = [1] * (n + 1) # 초기화

    for i in range(2, n + 1):
        dp[i] += dp[i-2]

    for i in range(3, n + 1):
        dp[i] += dp[i - 3]

    return dp[n]

n = int(stdin.readline())

for _ in range(n):
    target = int(stdin.readline())
    print(solution(target))