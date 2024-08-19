import sys
input = sys.stdin.readline

p, m = list(map(int, input().rstrip().split()))
rooms = []

for _ in range(p):
    l, n = list(input().rstrip().split())
    l = int(l)
    flag = False
    for room in rooms:
        key = room[0][0] # 기준 레벨
        if key - 10 <= l <= key + 10:
            if len(room) < m:
                room.append((l, n))
                flag = True
                break
    if not flag:
        rooms.append([(l, n)])

for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    for player in sorted(room, key=lambda x: x[1]):
        print(*player)