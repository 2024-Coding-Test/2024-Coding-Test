# 창고 다각형
# N개의 막대 기둥 일렬로 세워져 있음.
# 기둥들의 폭 모두 1m > 기둥을 이용하여 창고 제작
# 1. 지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
# 2. 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
# 3. 지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
# 4. 지붕의 가장자리는 땅에 닿아야 한다.
# 5. 비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.

from sys import stdin

N = int(stdin.readline())
roof = [0 for _ in range(1001)] # 기둥들의 높이를 저장
top = [-1, -1] # 가장 높은 건물의 위치와 높이를 저장
left = 1000 # 기둥의 시작 위치 저장
right = 0 # 기둥의 끝 위치 저장
result = 0 # 결과 저장

# 기둥들의 위치 및 높이를 입력받아 저장
for _ in range(N):
    L, H = map(int, stdin.readline().split())
    roof[L] = H
    left = min(left, L)
    right = max(right, L)

    # 가장 높은 건물 정보 업데이트
    if top[1] < H:
        top[0] = L
        top[1] = H
    elif top[1] == H:
        top[0] = max(top[0], L)

nowTop = roof[left] # 가장 왼쪽에서 top 전까지 현재 가장 높은 기둥 저장
for i in range(left, top[0]+1):
    if roof[i] > nowTop:
        nowTop = roof[i]
    result += nowTop
    # print(result)

nowTop = roof[right] # top부터 가장오른쪽까지 범위 중 현재 가장 높은 기둥 저장
for i in range(right, top[0], -1):
    if roof[i] > nowTop:
        nowTop = roof[i]
    result += nowTop
    # print(result)
print(result)
