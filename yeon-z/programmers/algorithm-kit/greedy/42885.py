# 구명보트
# 현재 코드
from collections import deque


def solution(people, limit):
    answer = 0

    # 보트에 한번에 2명만 가능
    # limit 보트 무게 제한

    people.sort(key=lambda x: -x)
    people = deque(people)

    while len(people) > 0:
        if len(people) > 1 and people[-1] + people[0] <= limit:
            people.popleft()
            people.pop()
            answer += 1
        else:
            people.popleft()
            answer += 1

    return answer

# 이전 코드
from collections import deque

def solution(people, limit):
    # 보트 한번에 2명만 가능
    # limit 보트 무게 제한

    people.sort(reverse=True)
    people = deque(people)
    cnt = 0

    while len(people) > 0:
        if len(people) == 1:
            cnt += 1
            people.popleft()
        elif people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            cnt += 1
        else:
            cnt +=1
            people.popleft()
    return cnt