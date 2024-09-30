from collections import deque
import sys
input = sys.stdin.readline

r,c = map(int,input().split())
maze = [list(input().strip()) for _ in range(r)]

# 지훈이는 한 칸씩 이동 가능, 불은 네 방향으로 퍼짐
# 불은 여러 곳에서 날 수 있음

q = deque()

# 지훈의 위치를 먼저 저장해야 지훈이 불 보다 먼저 움직일 수 있게 됨.
# 지훈이 불보다 먼저 움직여야 오류가 발생하지 않음. 불이 먼저 움직이면 지훈은 불이 오는데도 움직이지 않고 그대로 타죽어 버림
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            q.append([0,i,j])

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'F':
            q.append([-1,i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 'IMPOSSIBLE'

while q:
    cnt, x, y = q.popleft()

    # 탈출
    if cnt > -1 and maze[x][y] != 'F' and (x == 0 or y == 0 or x == r-1 or y == c-1):
        ans = cnt + 1
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] != '#':
            # 이동
            if cnt > -1 and maze[nx][ny] == '.':
                maze[nx][ny] = 'J'
                q.append([cnt+1,nx,ny])
            # 불 퍼짐
            elif cnt == -1 and maze[nx][ny] != 'F':
                maze[nx][ny] = 'F'
                q.append([-1,nx,ny])

print(ans)