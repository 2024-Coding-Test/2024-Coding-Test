t = int(input())
for _ in range(t):
    n = int(input())
    team = list(map(int,input().split()))
    
    for i in range(n):
        if team.count(team[i]) != 6:
            team[i] = 0

    team = [num for num in team if num != 0] # 선수가 6명 이상인 팀
    
    score = [i for i in range(1,len(team)+1)] # 등수
    
    grade = {num : [] for num in set(team)} # 각 팀 선수들의 등수
    total_score = {num : 0 for num in set(team)} # 각 팀의 상위 네 명의 선수들의 등수 합
    for i in range(len(team)):
        grade[team[i]].append(score[i])
    for key in total_score:
        total_score[key] = sum(grade[key][:4])

    answer = {}
    for key in total_score:
        if total_score[key] == min(total_score.values()):
            answer[key] = 6
    # 점수가 같은 팀이 있다면, 5번째로 들어온 선수의 등수가 더 높은 팀이 우승
    if len(answer) > 1:
        for n in team:
            if n in answer:
                answer[n] -= 1
                if answer[n] == 1:
                    print(n)
                    break
    else:
        print(list(answer.keys())[0])