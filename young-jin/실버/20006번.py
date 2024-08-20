import sys
input = sys.stdin.readline

p,m = map(int,input().split())
player = [list(input().strip().split()) for _ in range(p)]
room = {1 : [[player[0][0], player[0][1]]]}

for i in range(1,p):
    l,n = player[i]
    for k in room:
        refer = int(room[k][0][0])
        if refer-10 <= int(l) <= refer+10 and len(room[k]) < m:
            room[k].append(player[i])
            break
    if all(player[i] not in list(room.values())[j] for j in range(len(room))):
        room[list(room.keys())[-1]+1] = [player[i]]

for k in room:
    room[k] = sorted(room[k], key=lambda x : x[1])
    if len(room[k]) == m:
        print('Started!')
        for i in range(m):
            print(*room[k][i])
    else:
        print('Waiting!')
        for i in range(len(room[k])):
            print(*room[k][i])