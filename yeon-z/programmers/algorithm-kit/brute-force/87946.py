# 피로도
# 현재 코드
from itertools import permutations
def solution(k, dungeons):
    perms = list(permutations(dungeons))
    answer = -1

    for perm in perms:
        cnt = 0
        HP = k
        for p in perm:
            if HP >= p[0]:
                HP -= p[1]
                cnt += 1
        if cnt > answer:
            answer = cnt
        if answer == len(dungeons):
            return answer
    return answer

# 이전 코드
from itertools import permutations as p

def solution(k, dungeons):
    answer = -1
    m = 0
    l = len(dungeons)
    for o in p(range(l)):
        hp = k
        cnt = 0
        for n, i in enumerate(o):
            if hp >= dungeons[i][0]:
                cnt += 1
                hp -= dungeons[i][1]
        if cnt > answer:
            answer = cnt
    return answer