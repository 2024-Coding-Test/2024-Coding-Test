# 옛날 풀이
def solution(participant, completion):
    dict = {}
    for c in completion:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1

    for p in participant:
        if p not in dict:
            return p
        if p in dict:
            dict[p] -= 1
        if dict[p] < 0 :
            return p

# 현재 풀이
def solution(participant, completion):
    dict = {}
    for c in completion:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1

    for p in participant:
        if p not in dict:
            return p

        if dict[p] <= 0:
            return p
        else:
            dict[p] -= 1