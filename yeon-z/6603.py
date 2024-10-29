# 로또
from sys import stdin
from itertools import combinations

while True:
    arr = list(map(int, stdin.readline().split()))
    if arr[0] == 0:
        break
    k = arr[0]
    nSet = set(arr[1:])
    combi = list(combinations(nSet, 6))

    for idx in range(len(combi)):
        combi[idx] = list(combi[idx])
        combi[idx] = sorted(combi[idx])

    combi.sort()

    for c in combi:
        print(' '.join(map(str, c)))
    print()