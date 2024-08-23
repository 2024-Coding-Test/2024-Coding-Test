# 겹치는 건 싫어
# 수열에서 같은 원소가 여러 개 들어 있는 수열을 싫어함.
# 같은 원소가 K개 이하로 들어 있는 최장 연속 부분 수열의 길이를 구해라
# 100000 이하의 양의 정수로 이루어진 길이가 N인 수열이 주어짐
# 이 수열에서 같은 정수를 K개 이하로 포함한 최장 연속 부분 수열의 길이를 출력

# ex)
# 9 2
# 3 2 5 5 6 4 4 5 7
# 길이 N개 수열, K개 이하 => 길이 9개 수열, 2개 이하
# 출력 7

from sys import stdin
from collections import defaultdict

N, K = map(int, stdin.readline().strip().split())
arr = list(map(int, stdin.readline().strip().split()))

count = defaultdict(int)
left = 0
max_length = 0
over_count = 0  # K를 초과하는 빈도를 가진 원소의 개수

# 오른쪽 포인터를 이동시키며 윈도우 확장
for right in range(N):
    count[arr[right]] += 1

    if count[arr[right]] > K:
        over_count += 1

    while over_count > 0:
        if count[arr[left]] > K:
            over_count -= 1
        count[arr[left]] -= 1
        left += 1


    # 최대 길이 갱신
    max_length = max(max_length, right - left + 1)

print(max_length)