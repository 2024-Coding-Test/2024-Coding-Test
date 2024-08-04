from sys import stdin as s 

# s = open("input.txt", "rt")

T = int(s.readline())

for _ in range(T):
    N = int(s.readline())
    player = list(s.readline().strip().split())
    
    li = [i for i in player if player.count(i) >= 6]
    
    score_result = {}
    
    for i in range(len(li)):
        if li[i] not in score_result:
            score_result[li[i]] = [i+1]
        else:
            score_result[li[i]].append(i+1) 
    
    result = list(score_result.keys())
    result.sort(key=lambda x : (sum(score_result[x][:4]), score_result[x][4], score_result[x][5]))

    print(result[0])
