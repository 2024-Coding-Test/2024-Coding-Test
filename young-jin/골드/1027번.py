import sys
input = sys.stdin.readline

n = int(input())
height = list(map(int,input().split()))

ans = [0] * (n+1)
grad = [-1e9] * (n+1)
i = 0; j = 1
while i < n:

    if j == n:
        i += 1
        j = i+1
        grad = [-1e9] * (n+1)
        continue

    x1 = i; y1 = height[i]
    x2 = j; y2 = height[j]
    g = (y1-y2)/(x1-x2)
    g_before = grad[j-1]

    if g_before >= g:
        grad[j] = g_before
    else:
        grad[j] = g
        ans[i] += 1
        ans[j] += 1

    j += 1

print(max(ans))

# 기울기가 양수인 경우에는 기울기가 더 크거나 같을 때 가림
# 기울기가 음수인 경우에도 기울기가 더 크거나 같을 때 가림
# -> 기울기가 더 클 때 가림

# 만약 이전 건물 간의 기울기가 현재 건물 간의 기울기보다 크거나 같다면, 이전 건물이 가리고 있음
# -> 기준 기울기를 이전 건물 기준으로 설정
# 만약 이전 건물 간의 기울기가 현재 건물 간의 기울기보다 작다면, 이전 건물이 가리지 않음
# -> 기준 기울기를 현재 건물 기준으로 설정, 볼 수 있는 건물 +1, 현재 건물에서도 기준 건물을 볼 수 있음