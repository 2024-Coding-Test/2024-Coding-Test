import sys

N, K = map(int, sys.stdin.readline().strip().split())
medal = [[0, 0, 0, 0] for _ in range(N)]

for i in range(N):
    medal[i][0], medal[i][1], medal[i][2], medal[i][3] = map(int, sys.stdin.readline().strip().split())

medal.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

team_rank = [1] + [0 for _ in range(N-1)]
rank = 1

for i in range(1, N):
    if medal[i][1] == medal[i-1][1] and medal[i][2] == medal[i-1][2] and medal[i][3] == medal[i-1][3]:
        team_rank[i] = team_rank[i-1]
    else:
        rank = i + 1
        team_rank[i] = rank

for i in range(N):
    if medal[i][0] == K:
        print(team_rank[i])
        break