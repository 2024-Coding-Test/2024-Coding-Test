# 부분수열의 합
from sys import stdin
from itertools import combinations

N, S = map(int, stdin.readline().split())

arr = list(map(int, stdin.readline().split()))
answer = 0

for i in range(1, len(arr)):
    combi = list(combinations(arr, i))
    for c in combi:
        if sum(list(c)) == S:
            answer += 1
if sum(arr) == S:
    answer += 1
print(answer)


