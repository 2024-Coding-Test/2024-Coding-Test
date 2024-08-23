# KCPC
# 제출 팀 ID, 문제 번호, 점수 로그 시간 순서대로 저장
# 한문제 풀이 여러번 제출하면 최고 점수가 최종 점수가 된다.
# 팀 최종 점수는 모든 문제 점수 총합 > 순위는 당신 팀보다 높은 점수를 받은 팀의 수 + 1
# 점수 동일한 팀 여럿인 경우
# 1. 최종 점수가 같을 경우 > 풀이를 제출한 횟수가 적은 팀의 순위가 높음
# 2. 최종 점수도 같고 제출 횟수도 같은 경우 > 마지막 제출 시간이 빠른 팀의 순위가 높음

from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    # n 팀 수
    # pn 문제 수
    # tID 내 팀 ID
    # m 로그 수
    n, pn, tID, m = map(int, stdin.readline().strip().split())
    logs = []
    team = [{'c': 0, 'l': -1, 't': i+1, 's': 0 } for i in range(n)]
    for k in range(m):
        # 로그 입력 받기
        # i 팀 ID
        # j 문제 번호
        # s 점수
        i, j, s = map(int, stdin.readline().strip().split())
        logs.append([i, j, s])
        if j not in team[i-1]:
            team[i-1][j] = s
        else:
            team[i-1][j] = max(team[i-1][j],s)
        team[i-1]['c'] += 1 # 풀이 횟수
        team[i-1]['l'] = k
    for i in range(len(team)):
        score = 0
        for j in range(1, pn+1):
            if j in team[i]:
                score += team[i][j]
        team[i]['s'] = score

    team.sort(key=lambda x: [-x['s'], x['c'], x['l']])
    rank = 0
    # print(team)
    for t in team:
        rank += 1
        if t['t'] == tID:
            print(rank)
            break