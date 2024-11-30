from collections import deque

N,M,K = map(int,input().split())
map = [list(input()) for _ in range(N)]
S = [input() for _ in range(K)]

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,-1,1,1,-1]

X = [0] * (N+1) + [N-1]
Y = [0] * (M+1) + [M-1]
result = {}

# x,y : 좌표
# s : map[x][y]
# S[n] : S의 원소
def bfs(x,y):
    global ans
    queue = deque()
    s = map[x][y]
    queue.append((x,y,s))

    while queue:
        x,y,s = queue.popleft()

        if s in result:
            result[s] += 1
        else:
            result[s] = 1
        
        if len(s) >= 5:
            continue

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == -1 or nx == N:
                nx = X[nx]
            if ny == -1 or ny == M:
                ny = Y[ny]

            queue.append((nx,ny,s+map[nx][ny]))

for x in range(N):
    for y in range(M):
        bfs(x,y)

for s in S:
    if s in result:
        print(result[s])
    else:
        print(0)