from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
map = [list(input().strip()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

place = []
for i in range(N):
    for j in range(M):
        if map[i][j] == 'L':
            if 1 <= i < N-1 and 1 <= j < M-1:
                # 그래프에서 최단 경로의 거리가 최대가 되는 두 점은, 각각 상하로 1개 이하 및 좌우로 1개 이하의 연결점을 가지면서 상하좌우 중 적어도 하나의 연결점은 반드시 있는 점들
                if map[i-1][j] == 'L' and map[i+1][j] == 'L':
                    continue
                if map[i][j-1] == 'L' and map[i][j+1] == 'L':
                    continue
            place.append((i,j))

def bfs(i,j):
    queue = deque()
    queue.append((i,j))

    distance = [[0] * M for _ in range(N)]
    tmp = [row[:] for row in map]
    tmp[i][j] = 'V'
    
    result = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] == 'L':
                distance[nx][ny] = distance[x][y] + 1
                result = max(distance[nx][ny], result)

                tmp[nx][ny] = 'V'
                queue.append((nx,ny))

    return result

ans = 0
for p in place:
    i,j = p
    ans = max(ans,bfs(i,j))

print(ans)
