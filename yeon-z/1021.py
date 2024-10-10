# 유기농 배추
from sys import stdin
from collections import deque

input = stdin.readline

def get_position():
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                return (i, j)
    return (-1, -1)

def bfs(value):
    global ground
    start = get_position()

    queue = deque([start])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        ground[x][y] = value

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and ground[nx][ny] == 1:
                ground[nx][ny] = value
                queue.append((nx, ny))

    if get_position() != (-1, -1):
        bfs(value + 1)


T = int(input())

for _ in range(T):
    M, N, B = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    for _ in range(B):
        x, y = map(int, input().split())
        ground[y][x] = 1
    bfs(2)

    max_value = -1
    for g in ground:
        max_value = max(max_value, max(g))
    print(max_value - 1)