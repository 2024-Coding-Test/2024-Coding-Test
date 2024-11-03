from collections import deque

M,N,K = map(int,input().split())
graph = [[0] * N for _ in range(M)]
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    # range 함수가 '미만'까지 포함하는 것을 활용해서 좌표를 영역을 표현
    for i in range(x1,x2):
        # y좌표값이 리스트에서는 반대
        for j in range(M-y1-1, M-y2-1, -1):
            graph[j][i] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = []

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1
    size = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx,ny))
                size += 1
    result.append(size)

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            bfs(i,j)

result.sort()
print(len(result))
print(*result)