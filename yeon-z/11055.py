N = int(input())

arr = [0]

dp = [0] * (N + 1)

arr.extend(list(map(int, input().split())))

for i in range(1, N+1):
    temp = []
    for j in range(1, i):
        if arr[j] < arr[i]:
            temp.append(dp[j])
    if len(temp) > 0:
        dp[i] = max(temp) + arr[i]
    else:
        dp[i] = arr[i]

print(max(dp))