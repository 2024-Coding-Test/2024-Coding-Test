T = int(input())

arr = []

for _ in range(T):
    arr.append(int(input()))

dp = [0] * (max(arr) + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max(arr)+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


for a in arr:
    print(dp[a])