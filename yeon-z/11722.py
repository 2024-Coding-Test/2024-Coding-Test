N = int(input())

arr = list(map(int, input().split()))
arr.append(0)

arr = arr[::-1]

dp = [0] * (N  + 1)

for i in range(1, N + 1):
    temp = []
    for j in range(1, i):
        if arr[j] < arr[i]:
            temp.append(dp[j])
    if len(temp) > 0:
        dp[i] = max(temp) + 1
    else:
        dp[i] = 1
print(max(dp))