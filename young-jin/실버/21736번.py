import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
campus = [list(input().strip()) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = deque()
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            q.append((i,j))

answer = 0
while q:
    x,y = q.popleft()
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < N and 0 <= my < M:
            if campus[mx][my] == 'O':
                campus[mx][my] = 'X'
                q.append((mx,my))
            elif campus[mx][my] == 'P':
                answer += 1
                campus[mx][my] = 'O'
                q.append((mx,my))
            else:
                continue

if answer != 0:
    print(answer)
else:
    print('TT')