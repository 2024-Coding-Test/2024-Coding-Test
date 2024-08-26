# 컨베이어 벨트 위의 로봇
# 문제
# 길이가 N인 컨베이어 벨트가 있고, 길이가 2N인 벨트가 이 컨베이어 벨트를 위아래로 감싸며 돌고 있음.
# 벨트 길이 1간격으로 2N개의 칸으로 나뉘어져 있음. > 1 ~ 2N까지의 번호가 매겨져 있음.

# 벨트가 한 칸 회전하면 1번부터 2N-1번까지의 칸은 다음 번흐의 칸이 있는 위치로 이동하고, 2N번 칸은 1번 칸으로 이동
# i번 칸의 내구도 Ai
# 컨베이어 벨트에 박스 모양 로봇 올리려고 함(올리는 위치에서만 올릴 수 있음). 내리는 위치 도달하면 즉시 내림
# 로봇을 올리거나, 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1 감소
# 컨베이어 벨트를 이용해 로봇들을 건너편으로 옮기려고 함.

# 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
# 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동.
# 이동할 수 없다면 가만히 있는다.
# 2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1이상 남아있어야 함.
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
# 종료되었을 때 몇 번째 단계가 진행 중이었는지 구하기
# 가장 처음 수행되는 단계는 1번째 단계

# 2 ≤ N ≤ 100
# 1 ≤ K ≤ 2N
# 1 ≤ Ai ≤ 1,000

from sys import stdin

N, K = map(int, stdin.readline().split()) # N: 컨베이어 벨트 길이, K 내구도 0 개수

belts = []

A = list(map(int, stdin.readline().split())) # 내구도
for a in A:
    belts.append({
        'robot': False,
        'HP': a
    })

pRobot = []
step = 0
sIdx = 0
# print(belts)

while True:
    step += 1
    # print('=' * 10, step, '=' * 10)
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    sIdx = sIdx - 1 if sIdx - 1 >= 0 else len(belts) -1

    # print('1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전:: sIdx: ', sIdx)

    # DOWN위치에 로봇 있는지 확인
    DOWN = sIdx + (N-1) if sIdx + (N-1) < len(belts) else (sIdx + N - 1) % len(belts)
    if DOWN in pRobot:
        belts[DOWN]['robot'] = False
        pRobot.remove(DOWN)

    # print(' 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동. 이동할 수 없다면 가만히 있는다.')
    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동. 이동할 수 없다면 가만히 있는다.
    # 2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1이상 남아있어야 함.

    if (len(pRobot) > 0):
        # print('pRobot: ', pRobot)
        # 로봇이 있는 경우
        for p in list(pRobot):
            if p == DOWN:
                belts[p]['robot'] = False
                pRobot.remove(p)
            else:
                nP = p + 1

                if nP >= len(belts):
                    nP = 0

                if belts[nP]['HP'] > 0 and not belts[nP]['robot']:
                    belts[nP]['HP'] -= 1
                    belts[p]['robot'] = False
                    pRobot.remove(p)

                    if nP != DOWN:
                        belts[nP]['robot'] = True
                        pRobot.append(nP)
        # print('after pRobot: ',pRobot)
        # print('belts: ', belts)


    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if belts[sIdx]['HP'] > 0:
        belts[sIdx]['HP'] -= 1
        belts[sIdx]['robot'] = True
        pRobot.append(sIdx)
    # print(' 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.')
    # print(belts)
    # print(pRobot)


    cnt = 0
    for b in belts:
        if b['HP'] == 0:
            cnt += 1
    if cnt >= K:
        break


print(step)