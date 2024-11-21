import sys
from itertools import combinations
input = sys.stdin.readline

N,C = map(int,input().split())
W = list(map(int,input().split()))
A = W[:N//2]; B = W[N//2:]

s_A = []
for n in range(len(A)+1):
    comb = combinations(A,n)
    for c in comb:
        s_A.append(sum(c))

s_B = []
for n in range(len(B)+1):
    comb = combinations(B,n)
    for c in comb:
        s_B.append(sum(c))

# 이진 탐색을 위한 정렬
s_B.sort()
ans = 0
for a in s_A:
    if a > C:
        continue
    start = 0
    end = len(s_B)-1
    
    while start <= end:
        mid = (start+end) // 2
        if s_B[mid] + a > C:
            end = mid - 1
        else:
            start = mid + 1
    ans += end + 1

print(ans)