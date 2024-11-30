# 1로만 만들기 : dp를 1로 초기화
# 1,2로 만들기 : dp[i] += dp[i-2]
# 1,2,3으로 만들기 : dp[i] += dp[i-3]

import sys
input = sys.stdin.readline

t = int(input())
num = [int(input()) for _ in range(t)]

dp = [1] * (max(num)+1)

for i in range(2,len(dp)):
    dp[i] += dp[i-2]
for i in range(3,len(dp)):
    dp[i] += dp[i-3]

for n in num:
    print(dp[n])