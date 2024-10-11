# 헌내기는 친구가 필요해
from collections import deque
N, M = map(int, input().split())

campus = []
doyeon = (-1, -1)
persones = []

for i in range(N):
    arr = list(input())
    campus.append(arr)
    if 'P' in arr or 'I' in arr:
        for j in range(M):
            if arr[j] == 'I':
                doyeon = (i, j)
            elif arr[j] == 'P':
                persones.append((i, j))


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(doyeon, campus):
    q = deque([doyeon])
    visited = set()
    visited.add(doyeon)
    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and campus[nx][ny] != 'X' and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))
    return visited

visited = bfs(doyeon, campus)
cnt = 0
for p in persones:
    if p in visited:
        cnt += 1

if cnt > 0:
    print(cnt)
else:
    print('TT')