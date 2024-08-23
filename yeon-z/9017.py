# 한 팀은 6명
# 상위 네 명의 점수 합산
# 결승점을 통과한 순서대로 점수
# 점수의 합이 가장 낮은 팀이 우승

# T 테스트 케이스 수
# N 데이터의 수

from sys import stdin
T = int(stdin.readline().strip())

for _ in range(T):
    N = int(stdin.readline().strip())
    inputList = list(map(int, stdin.readline().strip().split()))
    ranking = []

    teamSet = list(set(inputList))
    # 팀에 6명이 없으면 ranking list에서 제거
    team = []
    for t in teamSet:
        if inputList.count(t) == 6:
            team.append(t)

    score = {}

    for t in team:
        score[t] = []

    for i in range(N):
        if inputList[i] in team:
            ranking.append(inputList[i])

    s = 1
    for r in ranking:
        score[r].append(s)
        s += 1

    scores = []
    for key in score.keys():
        score[key].append(sum(score[key][:4]))
        scores.append(sum(score[key][:4]))

    # print(score)
    minScore = min(scores)
    if scores.count(minScore) > 1:
        # 동점자 존재
        # key and 등수 저장
        keys = -1
        rank = 1000
        for key in score.keys():
            if score[key][-1] == minScore:
                if score[key][4] < rank:
                    rank = score[key][4]
                    keys = key
        print(keys)
    else:
        # print(score, minScore)
        for key in score.keys():
            if score[key][-1] == minScore:
                print(key)
                break
