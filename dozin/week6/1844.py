from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(maps):
    n, m = len(maps), len(maps[0])
    answer = 0
    queue = deque([(0,0)])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                maps[ny][nx] += maps[y][x]
                queue.append((ny, nx))
    return -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1]