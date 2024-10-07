from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())
walls = []

for _ in range(N):
    walls.append(list(map(int, input().strip())))

def bfs(graph, start):
    queue = deque([start])
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1 # 시작점 방문 표시

    # directions
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        x, y, flag = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y][flag]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 아니고 아직 방문하지 않은 경우
                if graph[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                    visited[nx][ny][flag] = visited[x][y][flag] + 1
                    queue.append((nx, ny, flag))
                # 벽이고 아직 벽을 부수지 않은 경우
                elif graph[nx][ny] == 1 and flag == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
    # 도달할 수 없을 경우
    return -1

print(bfs(walls, (0, 0, 0)))


# 7 4
# 0000
# 1110
# 1000
# 1000
# 0000
# 0111
# 0000
# answer: 10