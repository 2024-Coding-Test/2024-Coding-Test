import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    res[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    res[nx][ny] = 0
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    res[nx][ny] = res[x][y] + 1
                    queue.append((nx, ny))
    return


N, M = map(int, input().split(" "))
graph = list()
visited = [[0] * M for _ in range(N)]
res = [[-1] * M for _ in range(N)]

for i in range(N):
    A = list(map(int, input().rstrip().split(" ")))
    graph.append(A)
    if 2 in A:
        start_x = i
        start_y = A.index(2)

bfs(start_x, start_y)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end = " ")
        else:
            print(res[i][j], end = " ")
    print()
