# 같은 숫자는 싫어
# 현재 코드
def solution(arr):
    answer = []
    cur = arr[0]
    for a in arr[1:]:
        if a != cur:
            answer.append(cur)
            cur = a

    if (len(answer) != 0 and answer[-1] != cur) or len(answer) == 0:
        answer.append(cur)

    return answer


# 이전 코드
def solution(arr):
    # arr.sort(reverse=True)
    answer = []
    idx = 1
    target = arr[0]
    while idx < len(arr):
        if arr[idx] != target:
            answer.append(target)
            target = arr[idx]

        if idx == len(arr) - 1:
            answer.append(target)
        idx += 1

    return answer