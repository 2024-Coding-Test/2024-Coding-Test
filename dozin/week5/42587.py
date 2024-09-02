from collections import deque
def solution(prior,loc):
    answer = 0
    temp = deque(enumerate(prior)) 
    while temp:
        ord, prio = temp.popleft()
        if any(prio < temp_prio[1] for temp_prio in temp):
            temp.append((ord, prio))
        else:
            answer += 1
            if ord == loc:
                break
    return answer