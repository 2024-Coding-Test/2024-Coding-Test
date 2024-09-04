# 체육복
# 현재 코드
def solution(n, lost, reserve):
    answer = 0

    lost.sort()

    for idx, l in enumerate(lost):
        if l in reserve:
            reserve.remove(l)
            lost[idx] = -1
    for idx, l in enumerate(lost):
        # print(l, lost, reserve)
        if l == -1:
            pass
        elif l - 1 in reserve:
            reserve.remove(l - 1)
            lost[idx] = -1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            lost[idx] = -1

    lost = [i for i in lost if i != -1]

    return n - len(lost)

# 이전 코드
import copy
def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    temp = copy.deepcopy(lost)

    for idx in range(len(lost)):
        if lost[idx] in reserve:
            temp.remove(lost[idx])
            reserve.remove(lost[idx])

    lost = copy.deepcopy(temp)

    for l in lost:
        if l-1 in reserve:
            temp.remove(l)
            reserve.remove(l-1)
        elif l+1 in reserve:
            temp.remove(l)
            reserve.remove(l+1)

    return n - len(temp)