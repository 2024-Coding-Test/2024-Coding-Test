# 큰 수 만들기
# 현재 코드
def solution(number, k):
    number = [int(n) for n in number]
    answer = []

    idx = 0
    while idx < len(number) and k > 0:
        for j in range(idx + 1, len(number)):
            if number[j] > number[idx]:
                number.pop(idx)
                k -= 1
                idx = -1
                break
            else:
                break
        idx += 1

    if k > 0:
        number = number[:-k]

    return ''.join(map(str, number))


# 이전 코드
def solution(number, k):
    stack = []
    for n in number:
        if len(stack) == 0:
            stack.append(n)
        else:
            while True:
                if len(stack) == 0 or k == 0:
                    break
                if stack[-1] >= n:
                    break
                if stack[-1] < n and k > 0:
                    stack.pop()
                    k -= 1
            stack.append(n)

    if k > 0:
        while k > 0 :
            _min = min(stack)
            stack.remove(_min)
            k -= 1

    return "".join(stack)