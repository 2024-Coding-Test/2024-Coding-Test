# 진우의 달 여행(small)
# 지구 -> 달 은 위에서 아래로만 이동
# 전에 움직인 방향으로는 움직일 수 없음.
# 연료를 최대한 아끼며 달에 도착해야함.

from sys import stdin

N, M = map(int, stdin.readline().strip().split())
moon_map = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]

dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

for j in range(M):
    for k in range(3):
        dp[0][j][k] = moon_map[0][j]

for i in range(1, N):
    for j in range(M):
        for k in range(3):
            if k == 0 and j < M-1:
                dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + moon_map[i][j]
            elif k == 1:
                dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + moon_map[i][j]
            elif k == 2 and j > 0:
                dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + moon_map[i][j]

result = min(dp[N-1][j][k] for j in range(M) for k in range(3))
print(result)