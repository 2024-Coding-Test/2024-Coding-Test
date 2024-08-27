# 기능개발
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