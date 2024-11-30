import sys
input = sys.stdin.readline

n,c = map(int,input().split())
house = [int(input()) for _ in range(n)]

house = sorted(house)

# 가장 인접한 두 공유기 사이의 거리가 최대가 되어야 함
# 즉, 어떠한 두 공유기를 선택하더라도 그 사이의 거리가 최소 d 이상은 되어야 한다는 의미
# 거리 d를 설정하고, 해당 거리만큼 공유기를 설치했을 때 공유기를 c개 이상 설치할 수 있다면 거리가 너무 가까운 것
# 반대의 경우에는 거리가 너무 먼 것
# 거리를 기준으로 이분 탐색

start = 1; end = house[n-1] - house[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    current = house[0]
    count = 1

    for i in range(1, n):
        if house[i] >= current + mid:
            count += 1
            current = house[i]

    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)