# 참고해서 풀었음 > 나중에 다시 풀기

# 지름길
# 세준이 등교위해 D킬로미터 길이 고속도로 지남
# 지름길 존재 알게됨
# 모든 지름길 일방통행 역주행 ㄴㄴ
# 운전해야하는 최솟값 출력

# 지름길 개수 N, 고속도로 길이 D
# N은 12이하 양 정수, D는 10000 작거나 같은 자연수
# N개의 지름길의 시작위치, 도착위치, 지름길 길이 주어짐 # 모든 위치와 길이 10000보다 작거나 같은 음이 아닌 정수

from sys import stdin
N, D = map(int, stdin.readline().strip().split())

dp = [i for i in range(D + 1)] # 거리 저장

# 지름길 정보 저장
shortcuts = []
for _ in range(N):
    start, end, length = map(int, stdin.readline().strip().split()) # 시작위치, 종료위치, 거리
    # 지름길이 실제 고속도로보다 짧은 경우 지름길 후보로 추가
    if end - start > length:
        shortcuts.append([start, end, length])

# 지름길 출발 점 기준으로 정렬
shortcuts.sort(key=lambda x: x[0])

for start, end, length in shortcuts:
    # print('=' * 20)
    # print(start, end, length)
    for i in range(1, D+1):
        # print(i, dp[i])
        # 현재 위치가 지름길의 도착점이라면
        if end == i:
            # 현재 위치까지 오는 최소 시간은 기존 시간과 지름길을 이용한 시간을 비교하여 작은 값을 선택
            dp[i] = min(dp[i], dp[start] + length)
        else:
            dp[i] = min(dp[i], dp[i-1] + 1)
        # print(dp[i])
print(dp[D])