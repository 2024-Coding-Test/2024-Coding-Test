import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()
dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
answer = 0

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        a = A[i-1]; b = B[j-1]
        if a == b:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(answer)