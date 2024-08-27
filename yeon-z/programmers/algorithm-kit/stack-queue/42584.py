# 주식가격
# 현재 코드
def solution(prices):
    answer = []
    prices = prices[::-1]

    while len(prices) > 1:
        cur = prices.pop()
        time = 1
        for i in range(len(prices) - 1, 0, -1):
            if cur <= prices[i]:
                time += 1
            else:
                break
        answer.append(time)

    return answer + [0]

# 이전 코드
from collections import deque
def solution(prices):
    answer = []

    for i in range(len(prices)):
        cnt = 0
        for j in range(i, len(prices) - 1):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                break
        answer.append(cnt)

    return answer