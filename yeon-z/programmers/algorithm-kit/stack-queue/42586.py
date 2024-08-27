# 기능개발
# 현재코드
def solution(progresses, speeds):
    answer = []
    day = 0

    cnt = 0
    for i in range(len(progresses)):
        p = progresses[i]  # progress
        s = speeds[i]  # speed

        if (day * s) + p >= 100:
            cnt += 1
        else:
            t = ((100 - p) / s) if (100 - p) % s == 0 else ((100 - p) / s) + 1
            day = t
            if cnt != 0:
                answer.append(cnt)
            cnt = 1

        if i == len(progresses) - 1:
            answer.append(cnt)

    return answer


# 옛날 코드
import math


def solution(progresses, speeds):
    answer = []
    diff = []

    for idx in range(len(progresses)):
        diff.append(math.ceil((100 - progresses[idx]) / speeds[idx]))

    t = diff[0]
    cnt = 1
    for idx in range(1, len(diff)):
        if diff[idx] <= t:
            cnt += 1
        else:
            answer.append(cnt)
            t = diff[idx]
            cnt = 1

    answer.append(cnt)
    return answer