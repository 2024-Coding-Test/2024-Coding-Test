# 랭킹전 대기열
# 1. 플레이어가 입장을 신청하였을 때 매칭이 가능한 방이 없다면 새로운 방을 생성하고 입장시킨다.
# 1-1. 처음 입장한 플레이어의 레벨을 기준으로 -10부터 +10까지 입장 가능하다.
# 2. 입장 가능한 방이 있다면 입장시킨 후 방의 정원이 모두 찰 때까지 대기시킨다.
# 2-1. 이때 입장이 가능한 방이 여러개라면 먼저 생성된 방에 입장한다.
# 3. 방의 정원이 모두 차면 게임을 시작한다.

# 플레이어의 수 p
# 플레이어의 닉네임 n
# 플레이어의 레벨 l
# 방 한개의 정원 m

from sys import stdin

p, m = map(int, stdin.readline().strip().split())
room = []
# [처음 입장 레벨, [룸 참가한 사람]]

for _ in range(p):
    level, name = map(str, stdin.readline().strip().split())
    level = int(level)

    # 입장 가능한 방이 있는지 확인
    if len(room) > 0:
        flag = True # 입장했는지 룸 생성했는지 확인
        for r in room:
            # -10 +10 사이에 있으는지 확인 and 정원이 다 찼는지 확인
            if (r[0] - 10) <= level <= (r[0] + 10) and len(r[1]) < m:
                r[1].append([level, name])
                flag = False
                break

        if flag:
            # 룸 입장 못했으면 생성
            room.append([level, [[level, name]]])

    else:
        # 입장 가능한 방이 없으면 방 생성
        room.append([level, [[level, name]]])

for r in room:
    if len(r[1]) == m:
        print('Started!')
    else:
        print('Waiting!')
    r[1].sort(key=lambda x: x[1])
    for n in r[1]:
        print(n[0], n[1])