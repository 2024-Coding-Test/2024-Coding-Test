# 프로세스
# 현재 코드
from collections import deque


def solution(priorities, location):
    prio = list(set(priorities))
    prio.sort(key=lambda x: x)
    queue = deque([])

    cnt = 0
    idx = 0
    while len(queue) < len(priorities):
        if cnt == 0:
            p = prio.pop()
            cnt = priorities.count(p)

        if priorities[idx] == p:
            queue.append(idx)
            if idx == location:
                return len(queue)
            cnt -= 1
        idx = 0 if idx + 1 >= len(priorities) else idx + 1

# 이전 코드
def solution(priorities, location):
    answer = []

    priorities = [[priorities[idx], idx] for idx in range(len(priorities))]

    idx = 0
    while len(priorities) > 0:
        a = list(filter(lambda x: x[0] > priorities[idx][0], priorities))
        # print(priorities[idx][0], len(a), priorities)
        if len(a) > 0:
            tmp = priorities.pop(0)
            priorities.append(tmp)
        if len(a) == 0:
            answer.append(priorities[idx])
            priorities.pop(0)

    for idx in range(len(answer)):
        if answer[idx][1] == location:
            return idx+1
