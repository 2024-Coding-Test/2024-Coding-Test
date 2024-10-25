# 다리 놓기
T = int(input())

def bridge(n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, m+1):
        dp[1][i] = i # N이 1일 때

    # N이 2 이상일 때
    for i in range(2, n+1):
        for j in range(i, m+1):
            for k in range(j, i-1, -1):
                dp[i][j] += dp[i-1][k-1]
    return dp[n][m]

for _ in range(T):
    N, M = map(int, input().split())
    print(bridge(N,M))