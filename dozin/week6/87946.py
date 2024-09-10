from itertools import permutations

def solution(k, dungeons):
    answer = -1
    array = list(permutations(dungeons, len(dungeons)))
    
    for each in array:
        p = k
        check = 0
        for dungeon in each:
            if p >= dungeon[0]:
                p -= dungeon[1]
                check += 1
            else:
                continue
                
        if answer < check:
            answer = check
            
    return answer