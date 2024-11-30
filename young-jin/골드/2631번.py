N = int(input())
child = [int(input()) for _ in range(N)]

# 최장 증가 부분 수열 (LIS)
count = [1] * N
M = 0

for i in range(1,N):
    for j in range(i):
        if child[i] > child[j]:
            count[i] = max(count[i], count[j]+1)
    M = max(M, count[i])

print(N-M)