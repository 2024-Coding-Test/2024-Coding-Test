# 구슬 탈출 2
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
board = []

rx, ry, bx, by = 0, 0, 0, 0

for i in range(N):
    arr = list(stdin.readline().strip())
    board.append(arr)
    for j in range(M):
        if 'R' in arr or 'B' in arr:
            if 'R' == arr[j]:
                rx, ry = i, j # 빨간구슬 위치
            if 'B' == arr[j]:
                bx, by = i, j # 파란구슬 위치

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move(x, y, dx, dy):
    count = 0
    # print(x, y, dx, dy, board[x][y])

    while board[x+dx][y+dy] != '#':
        x += dx
        y += dy
        count += 1

        if board[x][y] == 'O':
            return x, y, count, True
    return x, y, count, False

def bfs(rx, ry, bx, by):
    q = deque([(rx,ry,bx,by,1)])

    visited = set()
    visited.add((rx,ry,bx,by))

    while q:
        rx,ry,bx,by,depth = q.popleft()

        if depth > 10:
            return -1

        for dx, dy in directions:
            nrx, nry, rc, rflag = move(rx, ry, dx, dy)
            nbx, nby, bc, bflag = move(bx, by, dx, dy)
            # print('red',nrx, nry, rc, rflag)
            # print('blue',nbx, nby, bc, bflag)
            # print()

            if bflag and rflag:
                continue
            if bflag:
                continue
            if rflag:
                return depth
            if nrx == nbx and nry == nby:
                if rc < bc:
                    nbx -= dx
                    nby -= dy
                else:
                    nrx -= dx
                    nry -= dy

            if board[nbx][nby] == 'O':
                return -1
            if board[nrx][nry] == 'O':
                return depth

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx,nry,nbx,nby,depth + 1))
    return -1


print(bfs(rx, ry, bx, by))