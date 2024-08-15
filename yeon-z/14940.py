# 쉬운 최단거리
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().strip().split())
maps = []
start =[]

direction = [[-1, 0], [1,0], [0, -1], [0, 1]]

dist = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def bfs(x, y):
    global maps
    global dist
    global visited
    global direction

    queue = deque()
    queue.append([x, y])

    while len(queue) > 0:
        x, y = queue.popleft()
        # print(x,y)
        # print(queue)
        # print()
        visited[x][y] = True

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1 and dist[nx][ny] == 0:
                queue.append([nx, ny])
                dist[nx][ny] = dist[x][y] + 1

for i in range(n):
    row = list(map(int, stdin.readline().strip().split()))
    maps.append(row)
    if 2 in row:
        start.append(i)
        start.append(row.index(2))

bfs(start[0], start[1])

# print(visited)

for i in range(len(visited)):
    for j in range(len(visited[0])):
        if not visited[i][j] and maps[i][j] == 1:
            dist[i][j] = -1

for d in dist:
    print(*d)