from sys import stdin
from collections import deque
input = stdin.readline


M, N = map(int, input().split())
# M 가로, N 세로
tomatoes = []
set_tomatoes = set()
day = 0

for _ in range(N):
    inputs = list(map(int, input().split()))
    set_tomatoes.update(set(inputs))
    tomatoes.append(inputs)

# 현재 모든 토마토가 있었는지 확인하기
if len(set_tomatoes) == 1 and set_tomatoes.pop() == 1:
    print(0)
    exit()

# 익은 토마토가 없는 경우
if 1 not in set_tomatoes:
    print(-1)
    exit()

queue = deque([])

# 익은 토마토들 queue에 담기
for x in range(N):
    for y in range(M):
        if tomatoes[x][y] == 1:
            queue.append((x, y))

# bfs
def bfs(graph, queue):
    # 상 하 좌 우
    directionX = [-1, 1, 0, 0]
    directionY = [0, 0, -1, 1]

    next = deque([])

    while queue:
        x, y = queue.popleft()
        for i in range(len(directionX)):
            nx, ny = x + directionX[i], y + directionY[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                next.append((nx, ny))
    return graph, next

while queue:
    tomatoes, queue = bfs(tomatoes, queue)
    day += 1

for tomato in tomatoes:
    # 익지 않은 토마토가 있는지 확인
    if 0 in tomato:
        print(-1)
        exit()
print(day - 1)