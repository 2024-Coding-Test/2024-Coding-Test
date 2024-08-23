# 예산
# 가능한 한 최대의 총 예산
# 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정
# 모든 요청이 배정될 수 없는 경우 특정한 정수 상한액을 계산하여, 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정

from sys import stdin

n = int(stdin.readline())
money = list(map(int, stdin.readline().split()))
max_money = int(stdin.readline())

start, end = 0, max(money)
mid = 0

while start < end:
    mid = (start + end) // 2

    if start == mid:
        break
    total = 0
    for m in money:
        if m <= mid:
            total += m
        else:
            total += mid
    if total > max_money:
        end = mid
    elif total == max_money:
        break
    else:
        start = mid
    prev = mid

if mid != end:
    total = 0
    for m in money:
        if m <= end:
            total += m
        else:
            total += end
    if total <= max_money:
        print(end)
    else:
        print(mid)
else:
    print(mid)