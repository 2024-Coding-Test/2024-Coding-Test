from collections import deque

N = int(input())
grid = [list(input()) for _ in range(N)]
grid2 = [row[:] for row in grid]
for i in range(N):
    for j in range(N):
        if grid2[i][j] == 'G':
            grid2[i][j] = 'R'

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j,grid):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True  
    while queue:
        x,y = queue.popleft()
        color = grid[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and color == grid[nx][ny] and visited[nx][ny] == False:
                queue.append((nx,ny))
                visited[nx][ny] = True

region1 = 0; region2 = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i,j,grid)
            region1 += 1
            
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i,j,grid2)
            region2 += 1

print(region1, region2)