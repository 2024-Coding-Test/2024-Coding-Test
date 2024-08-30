# H-Index
# 현재 코드
def solution(citations):
    # n 편 중 h번 이상 인용된 논문이 h편 이상
    # h의 최대 값
    answer = 0
    citations.sort()

    for h in range(1, citations[-1] + 1):
        cnt = 0
        for i in range(len(citations)):
            if citations[i] >= h:
                cnt = len(citations) - i
                break
        if cnt >= h:
            answer = h
    return answer
# 이전 코드
def solution(citations):
    answer = 0
    n = len(citations)
    _max = max(citations)

    for h in range(_max):
        cnt = 0
        for c in citations:
            if c >= h:
                cnt += 1
        if cnt >= h:
            answer = h
    return answer