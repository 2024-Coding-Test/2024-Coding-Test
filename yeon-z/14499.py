# 주사위 굴리기
from sys import stdin

input = stdin.readline

N, M, x, y, k = map(int, input().split())
maps = []

for _ in range(N):
    maps.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

up = 0
down = 0
right = 0
front = 0
back = 0
left = 0

SOUTH, NORTH, EAST, WEST = 4, 3, 1, 2

# SOUTH => front
# NORTH => back
# EAST => left
# WEST => right

positions = (x, y)

for c in commands:

    # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
    # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
    if c == SOUTH:
        nx, ny = positions[0] + 1, positions[1]
    elif c == NORTH:
        nx, ny = positions[0] - 1, positions[1]
    elif c == WEST:
        nx, ny = positions[0], positions[1] -1
    else:
        nx, ny = positions[0], positions[1] + 1

    # 범위 넘어가면 아무것도 안함
    if 0 <= nx < N and 0 <= ny < M:
        positions = (nx, ny)
    else:
        continue

    if c == SOUTH:
        tmp = front
        front = up
        up = back
        back = down
        down = tmp
    elif c == NORTH:
        tmp = up
        up = front
        front = down
        down = back
        back = tmp
    elif c == WEST:
        tmp = left
        left = up
        up = right
        right = down
        down = tmp
    else:
        tmp = right
        right = up
        up = left
        left = down
        down = tmp

    if maps[nx][ny] == 0:
        maps[nx][ny] = down
    else:
        down = maps[nx][ny]
        maps[nx][ny] = 0
    # print()
    # print(' ', back)
    # print(left, up, right)
    # print(' ', front)
    # print(' ', down)
    print(up)