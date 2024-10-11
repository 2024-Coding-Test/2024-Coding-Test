from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())

red_x, red_y = 0, 0
blue_x, blue_y = 0, 0

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = []
for i in range(N):
    arr = list(input().strip())
    if 'R' in arr or 'B' in arr:
        for j in range(M):
            if arr[j] == 'R':
                red_x = i
                red_y = j
            elif arr[j] == 'B':
                blue_x = i
                blue_y = j
    board.append(arr)
def move(x, y, dx, dy, board):
    count = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs(rx, ry, bx, by):
    q = deque([])
    q.append((rx, ry, bx, by, 1)) # 1은 초기 이동 횟수

    visited = set()
    visited.add((rx, ry, bx, by))

    while q:
        rx, ry, bx, by, depth = q.popleft()

        if depth > 10:
            return -1

        for dx, dy in directions:
            nrx, nry, rc = move(rx, ry, dx, dy, board)
            nbx, nby, bc = move(bx, by, dx, dy, board)

            if board[nbx][nby] == 'O': # 파란 구슬이 구멍에 빠지면 실패
                continue
            if board[nrx][nry] == 'O': # 빨간 구슬이 구멍에 빠지면 성공
                return depth

            if nrx == nbx and nry == nby: # 두 구슬이 같은 위치에 있으면
                if rc > bc:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth + 1))
    return -1

print(1 if bfs(red_x, red_y, blue_x, blue_y) > -1 else 0)